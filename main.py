from hashlib import md5
import random

def md125(s: str) -> str: # this is the hash function you'll use
  return md5(s.encode()).hexdigest()[:8]

def random_string():

  s = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(10)])

  return s

def generate_md125_collisions() -> (str, str):

  digests = {}

  while True:

    pre_image = 'nakamoto' + random_string()
    digest = md125(pre_image)

    if(digests.get(digest, None) != None):
      return (digests[digest], pre_image)
    else:
      digests[digest] = pre_image
  
  pass 

if __name__ == '__main__':

  generate_md125_collisions()