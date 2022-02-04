

def remove(input_file):
    print(input_file)
    output_file = input_file + "_deseg"
    with open(input_file, "r", encoding="utf8") as fr:
        with open(output_file, "w", encoding="utf8") as fw:
            for line in fr:
                line = line.strip()
                if len(line) == 0:
                    fw.write("\n")
                else:
                    line_split = line.split("\t")
                    fw.write(line_split[0][:1] + "\t" + line_split[1] + "\n")


if __name__ == '__main__':
    remove("./data/weiboNER_2nd_conll.train")
    remove("./data/weiboNER_2nd_conll.dev")
    remove("./data/weiboNER_2nd_conll.test")
