def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We don't know that flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Next customer please")


order = ["masala", "unknown", "ginger", "chocolate"]
print("----------------------------")
for flavor in order:
    serve_chai(flavor)
    print("----------------------------")

