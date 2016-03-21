import os
import zipfile
from contextlib import closing
from zipfile import ZipFile, ZIP_DEFLATED


def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))


def zipdir2(basedir, archivename):
    assert os.path.isdir(basedir)
    with closing(ZipFile(archivename, "w", ZIP_DEFLATED)) as z:
        for root, dirs, files in os.walk(basedir):
            # NOTE: ignore empty directories
            for fn in files:
                absfn = os.path.join(root, fn)
                zfn = absfn[len(basedir) + len(os.sep):]  # XXX: relative path
                z.write(absfn, zfn)


print("Zip dir...")

zipf = zipfile.ZipFile('c:/temp/txt.zip', 'w')
zipdir('c:/temp/txt', zipf)
zipf.close()

#########

print("zip dirs...")

zipdir2('c:/temp/txt', 'c:/temp/txt2.zip')

zipdir2('c:/temp/Docs', 'c:/temp/docs2.zip')

zipdir2('c:/temp/ROOT/', 'c:/temp/root.zip')

print("complete")