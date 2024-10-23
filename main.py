# stable_marriage.py

def stable_marriage(n, boy_preferences, girl_preferences):
  boy_to_girl = {}
  boy_proposed = {i+1: 0 for i in range(n)}
  girl_to_boy = {}

  while len(boy_to_girl) < n:
    for i in range(n):
      current_boy = i + 1
      if current_boy not in boy_to_girl:
        current_boy_preference = boy_preferences[i]
        index = boy_proposed[current_boy]
        boy_proposed[current_boy] += 1
        current_girl = current_boy_preference[index]
        boy_to_girl[current_boy] = current_girl
      
        if current_girl not in girl_to_boy:
          girl_to_boy[current_girl] = current_boy
        else:
          current_girl_preference = girl_preferences[current_girl - 1]
          boy = girl_to_boy[current_girl]
          if current_girl_preference.index(boy) > current_girl_preference.index(current_boy):
            girl_to_boy[current_girl] = current_boy
            del(boy_to_girl[boy])
          else:
            del(boy_to_girl[current_boy])

  return boy_to_girl

