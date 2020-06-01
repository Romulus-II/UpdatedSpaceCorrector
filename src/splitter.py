import wordninja

class Splitter:
    def __init__(self, stop_words):
        self.stop_words = stop_words


    def split_line(self, line):
        words = line.split()
        new_line = ''
        for word in words:
            # Check if the word is not a stop word
            if word not in self.stop_words:
                split_words = wordninja.split(word)
                # Check if a word has actually been split
                if len(split_words) > 1:
                    output = split_words[0]
                    for i in range(1 , len(split_words)):
                        output_args = (output, split_words[i])
                        output = ' '.join(output_args)
                # Output both words to new file
                print(word, " -> ", output)
                new_line += output
        return new_line
