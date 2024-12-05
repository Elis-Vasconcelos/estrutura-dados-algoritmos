class Node:
  def __init__(self, symbol, letter):
      self.symbol = symbol
      self.letter = letter
      self.next = None
      self.prev = None


class CircularLinkedList:
  def __init__(self):
    self.head = None
    self.substitution_dict = {}
    
  def __iter__(self):
    current = self.head
    if current is not None:
        yield current
        while current.next != self.head:
            current = current.next
            yield current

  def contains(self, symbol):
    current = self.head
    if current is not None:
        if current.symbol == symbol:
            return True
        while current.next != self.head:
            current = current.next
            if current.symbol == symbol:
                return True
    return False

  def new_list(self):
      self.head = None

  def append(self, symbol, letter):
      new_node = Node(symbol, letter)
      if not self.head:
          self.head = new_node
          new_node.next = self.head
          new_node.prev = self.head
      else:
          current = self.head
          while current.next != self.head:
              current = current.next
          current.next = new_node
          new_node.prev = current
          new_node.next = self.head
          self.head.prev = new_node

  def free_list(self):
      if self.head is not None:
          current = self.head
          while True:
              current.prev = None
              if current.next is None:
                  break
              current = current.next

  def decrypt(self, encrypted_word, key):
      decrypted_word = ''
      for symbol in encrypted_word:
          current = self.head
          while current.symbol != symbol:
              current = current.next
          decrypted_word += current.letter
      return decrypted_word

  def create_substitution_dict(self):
    self.substitution_dict = {}
    for _ in range(26):
        symbol_letter = input().split()
        symbol = symbol_letter[0]
        letter = symbol_letter[1]
        self.substitution_dict[symbol] = letter

  def decrypt_word(self, roman_word, cesar_key):
    decrypted_word = ''
    for symbol in roman_word:
        if symbol in self.substitution_dict:
            letter = self.substitution_dict[symbol]
            decrypted_word += letter
    return decrypted_word


substitution_alphabet = CircularLinkedList()
for _ in range(26):
  symbol_letter = input().split()
  symbol = symbol_letter[0]
  letter = symbol_letter[1]
  substitution_alphabet.append(symbol, letter)

cesar_key = int(input())
encrypted_word = input()
roman_word = input()

decrypted_roman_word = substitution_alphabet.decrypt(encrypted_word, cesar_key)
decrypted_substitution_word = substitution_alphabet.decrypt_word(roman_word, cesar_key)

print(decrypted_roman_word)
print(decrypted_substitution_word)

substitution_alphabet.free_list()