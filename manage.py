import sys
import utils


if len(sys.argv) == 1:
    print("""Usage:
    Rebuild site: python manage.py build
    Create new page: python manage.py new""")
else:
    command = sys.argv[1]
    if command == "build":
        print("Build was specified")
        utils.main()
    elif command == "new":
        print("New page was specified")
        utils.new_content()
    else:
        print("Please specify ’build’ or ’new’")




