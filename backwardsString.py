def reverse_string(s):
    count = 1
    new = ""
    if len(s) == count:
        print "Please enter a valid string!"
    else:
        while count < (len(s) + 1):
            new += s[len(s) - count]
            count += 1
            print new
    # Test for python version then ask for string to reverse
    py3 = version_info[0] > 2
    if py3:
        response = input("Please enter a string to reverse: ")
    else:
        response = raw_input("Please enter a string to reverse: ")
reverse_string(response)
