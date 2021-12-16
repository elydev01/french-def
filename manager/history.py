import json
import os


class History:
    @classmethod
    def get_history_filename(cls):
        folder = os.path.expanduser("~")
        file = os.path.join(folder, ".his.json")
        return file

    @classmethod
    def get_history_data(cls):
        file = cls.get_history_filename()
        try:
            with open(file) as f:
                data = json.loads(f.read())
                assert isinstance(data, list)
                return data
        except Exception:
            return []

    @classmethod
    def add_new_item(cls, name):
        datas = cls.get_history_data()
        if name not in datas:
            datas.append(name)
            cls.save_new_update(datas)
            return True
        return False

    @classmethod
    def save_new_update(cls, datas):
        file = cls.get_history_filename()
        with open(file, "w") as f:
            f.write(json.dumps(datas))

    @classmethod
    def clear_all(cls):
        cls.save_new_update([])
