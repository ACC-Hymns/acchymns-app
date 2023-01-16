from shutil import copytree, rmtree, copy
import rcssmin
import json
import os.path
def ignorePaths(paths):
    abspaths = [os.path.abspath(path) for path in paths]
    def ignoref(directory, contents):
        return [f for f in contents if abspaths.count(os.path.abspath(os.path.join(directory, f))) > 0]
    return ignoref

src = "acchymns-web"
dest = "www"
if os.path.exists(dest) and os.path.isdir(dest):
    print("Removing previous directory...")
    rmtree(dest)

# Copy everything except book data
print("Copying all program data...")
copytree(src, dest, ignore=ignorePaths([f"{src}/books", ".git", ".gitignore"]))

for content in os.scandir(os.path.join(src, "books")):
    tobeDestPath = os.path.join(os.path.abspath(dest), os.path.relpath(content.path, os.path.abspath(src)))
    if content.is_dir():
        with open(os.path.join(content.path, "summary.json")) as summary_info:
            if not json.load(summary_info)["addOn"]:
                # Copy non add-on book
                print(f"Copying {content.name} images...")
                copytree(content.path, tobeDestPath)
    else:
        copy(content, tobeDestPath)

from pathlib import Path

def minifyFiles(pattern, minify_func, path_as_param=False):
    files = Path(dest).glob(pattern)
    for file in files:
        print(f"\tMinifying: {file.name}")
        if path_as_param:
            minify_func(file.absolute())
        else:
            try:
                with open(file) as unminified_file:
                    unminified = unminified_file.read()

                minified = minify_func(unminified)

                with open(file, "w") as minified_file:
                    minified_file.write(minified)
            except UnicodeDecodeError:
                print(f"\tFailed to minify {file.name}")

print("Minifying CSS files...")
minifyFiles("**/*.css", rcssmin.cssmin)

print("Minifying JS files...")
minifyFiles("**/*.js", lambda path: os.system(f"uglifyjs {path} -c -m -o {path}"), path_as_param=True)

print("Minifying JSON files...")
minifyFiles("**/*.json", lambda data: json.dumps(json.loads(data), separators=(',', ':')))

