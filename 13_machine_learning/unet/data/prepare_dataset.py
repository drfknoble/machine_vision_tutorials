from absl import app, flags
import pathlib

FLAGS = flags.FLAGS
flags.DEFINE_string("path", None, "C:/users/fraze/downloads")

def main(argv):

    # list_of_files = list(pathlib.Path(FLAGS.path).glob("*.*"))

    # print(str(list_of_files))

    return


if __name__ == "__main__":

    app.run(main)