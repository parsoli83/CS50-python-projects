match input("File name: ").lower().strip().split(".")[-1]:
    case "gif":
        print("image/gif")
    case "png":
        print("image/png")
    case "jpg":
        print("image/jpeg")
    case "jpeg":
        print("image/jpeg")
    case "txt":
        print("text/plain")
    case "pdf":
        print("application/pdf")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")