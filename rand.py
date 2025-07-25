try:
            with open('text.txt', 'r') as f:
                self.lists = f.readlines()
            if self.counter == 0:
                self.lists = [line.strip() for line in self.lists]
            elif self.counter >= 1:
                self.lists = [line + '\n' for line in self.lists]
        except FileNotFoundError:
            pass



                                self.lists.append(addition + '\n')
