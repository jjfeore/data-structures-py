end = '$'


class TrieTree(object):

    def __init__(self):
        """This will implement our Trie tree funciton."""
        self.size = 0
        self.root_set = []
        self.letter_sets = []

    def insert(self, *words):
        for word in words:
            current_letter_set = []
            self.size = self.size + 1
            if self.letter_sets == []:
                self.letter_sets.append(word)
                self.root_set = self.letter_sets[0]
                return self.letter_sets
                break

            else:
                import pdb; pdb.set_trace()
                dict_check = []
                for i in self.letter_sets:
                    dict_check.append(i)
                list_check = []
                letter_check = ''
                for curr_set in self.letter_sets:
                    if type(curr_set) == str:
                        list_check = curr_set
                    if type(curr_set) == dict:
                        for item in list(curr_set.keys()):
                            if type(item) == str:
                                list_check.append(item)
                        for thing in list_check:
                            if word[0] in thing:
                                for letter in word:
                                    letter_check = letter_check + letter
                                    if letter_check == thing:
                                        new_level = list(curr_set.values())
                                        current_letter_set = letter_check
                                        new_letter_set = []
                                        old_letter_set = []
                                        [new_letter_set.append(letter) for letter in word if letter not in current_letter_set]
                                        new_group_set = ''.join(new_letter_set)
                                        [old_letter_set.append(old) for old in self.letter_sets[0] if old not in current_letter_set]
                                        old_group_set = ''.join(old_letter_set)
                                        if current_letter_set != '':
                                            if current_letter_set == item:
                                                tmp = []
                                                [tmp.append(letter) for letter in word if letter not in current_letter_set]
                                                tmp = ''.join(tmp)
                                                if tmp == item:
                                                    continue
                                                else:
                                                    count = -1
                                                    for group in new_level[0]:
                                                        count += 1
                                                        if tmp[0] in group:
                                                            del_letters = ''
                                                            for tmp_letter in tmp:
                                                                del_letters = del_letters + tmp_letter
                                                                if del_letters == group:
                                                                    level_3 = []
                                                                    [level_3.append(char) for char in tmp if char not in group]
                                                                    level_3_group = ''.join(level_3)
                                                                    new_level[0][count] = {group: level_3_group}
                                                                    if count > -1:
                                                                        count = -1
                                                                else:
                                                                    if del_letters in group:
                                                                        continue
                                                    if tmp[0] not in new_level[0]:
                                                        new_level[0].append(tmp)

                                            else:
                                                if new_group_set or old_group_set != '':
                                                    if self.root_set in self.letter_sets:
                                                        self.letter_sets.remove(self.root_set)
                                                        self.root_set = self.letter_sets
                                                    if old_group_set not in self.letter_sets:
                                                        new_level.append(old_group_set)
                                                    if new_group_set not in self.letter_sets:
                                                        new_level.append(new_group_set)
                                                if '' in self.letter_sets:
                                                    self.letter_sets.remove('')
                                        return self.letter_sets
                                        break

                                    else:
                                        if letter_check in item:
                                            continue
                            else:
                                self.letter_sets.append({word: ''})
                                return self.letter_sets

        else:
            for letter in word:
                letter_check = letter_check + letter
                if letter_check in curr_set:
                    continue
                else:
                    new_level = []
                    current_letter_set = letter_check[:-1]
                    new_letter_set = []
                    old_letter_set = []
                    [new_letter_set.append(letter) for letter in word if letter not in current_letter_set]
                    new_group_set = ''.join(new_letter_set)
                    [old_letter_set.append(old) for old in self.letter_sets[0] if old not in current_letter_set]
                    old_group_set = ''.join(old_letter_set)
                    if current_letter_set in self.letter_sets and current_letter_set != '':
                        if current_letter_set == curr_set:
                            tmp = []
                            [tmp.append(letter) for letter in word if letter not in current_letter_set]
                            tmp = ''.join(tmp)
                            # new_level.append([tmp])

                    # else:
                        # self.letter_sets.append(current_letter_set)
                    if new_group_set or old_group_set != '':
                        if self.root_set in self.letter_sets:
                            self.letter_sets.remove(self.root_set)
                            self.root_set = self.letter_sets
                        if old_group_set not in self.letter_sets:
                            new_level.append(old_group_set)
                            # self.letter_sets.append(old_group_set)
                        if new_group_set not in self.letter_sets:
                            new_level.append(new_group_set)
                            # self.letter_sets.append(new_group_set)
                    if '' in self.letter_sets:
                        self.letter_sets.remove('')
                    self.letter_sets.append({current_letter_set: new_level})
                    return self.letter_sets

    def print_tree(self):
        count = 0
        for item in self.letter_sets:
            count += 1
            return 'Set ' + str(count) + ' ' + str(item)
    # def insert(self, word):
    #     for word in words:
    #         current_letter_set = []
    #         self.size = self.size + 1
    #         # word_dict = new_dict
    #         if self.letter_sets == []:
    #             self.letter_sets = [word]
    #             self.root_set = self.letter_sets
    #             return self.letter_sets
    #             break
    #         else:
    #             letter_check = ''
    #             for letter in word:
    #                 self.letters = self.letters + 1
    #                 letter_check = letter_check + letter
    #                 for lset in self.letter_sets:
    #                     if letter_check in lset:
    #                         good_group = letter_check
    #                         continue
    #                     else:
    #                         import pdb; pdb.set_trace()
    #                         current_letter_set = good_group
    #                         new_letter_set = []
    #                         old_letter_set = []
    #                         [new_letter_set.append(letter) for letter in word if letter not in current_letter_set]
    #                         new_group_set = ''.join(new_letter_set)
    #                         [old_letter_set.append(old) for old in self.letter_sets[0] if old not in good_group]
    #                         old_group_set = ''.join(old_letter_set)
    #                         self.letter_sets = [current_letter_set]
    #                         self.letter_sets.append(old_group_set)
    #                         self.letter_sets.append(new_group_set)
    #                         return self.letter_sets

    # def search(self, word):
    #     """."""
    #     current_word_dict = self
    #     for letter in word:
    #         if letter in current_word_dict:
    #             current_word_dict = current_word_dict[letter]
    #         else:
    #             return False
    #     else:
    #         if end in current_word_dict:
    #             return True
    #         else:
    #             return False
