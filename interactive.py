
def main():
  proceed = raw_input("'q' to quit, any other key to process next page :")
  print(proceed)
  if proceed == "q":
     exit()

  main()

main()
