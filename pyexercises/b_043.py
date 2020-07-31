def get_profile(*args, name="julian", profession="programmer", **kwargs):
    if args:
        print("no fucking thank you")
    elif not kwargs.keys():
        print(f"{name} is a {profession}")
    else:
        print("too much shit, stupid")


get_profile(name='bob', toes="ASS", profession='bitchboy', another_flag=False)
print()
get_profile(name='bob', profession='bitchboy')
print()
get_profile('julian')