import os

"""
EXECUTE THIS SCRIPT IN PROJECT ROOT DIRECTORY!
"""

INPUT_DIR = os.path.join('res', 'ui')
OUTPUT_DIR = os.path.join('app', 'view', 'ui')


def uic():
    print('start uic')
    cnt = 0
    for root, _, files in os.walk(INPUT_DIR):
        for file in files:
            if not file.endswith('.ui'):
                continue
            cnt += 1
            input_file = os.path.join(root, file)
            output_file = os.path.join(OUTPUT_DIR, file).removesuffix('.ui') + '.py'
            cmd = f'pyside6-uic {input_file} -o {output_file}'
            print('[%d] input: %s -> output: %s' % (cnt, input_file, output_file))
            os.system(cmd)
    print('finish uic -> overall %d files' % cnt)


if __name__ == '__main__':
    uic()
