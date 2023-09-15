from pathlib import Path

path = Path()
# if(path.exists()):
#     path.rmdir()
# else:
#     print(path.mkdir())
for file in path.glob('*'):
    print(file)

