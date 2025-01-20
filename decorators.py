def announce(f):
    def wrapper():
        print("Announcing...")
        f()
        print("Done with the function")
    return wrapper  


@announce
def hello():
    print("Hello, world!")

hello()