from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("--files", nargs="+", help="список файлов для обработки")
parser.add_argument("--report", nargs=1, help="тип отчёта")

args = parser.parse_args()

file_names = args.files
type_report = args.report
