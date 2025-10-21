from lesson_29.src.database import Database

def run():
    db = Database()
    if not db.connect():
        raise SystemExit("DB connect failed")

    db.create_table()
    uid = db.insert_user("Alice", 30)
    db.update_user_age(uid, 31)
    user = db.get_user(uid)
    print("USER:", user)
    db.delete_user(uid)
    db.close()

if __name__ == "__main__":
    run()
