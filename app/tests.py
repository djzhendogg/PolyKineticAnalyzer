import customtkinter as ctk

class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("400x400")
        self.root.title("File Manager")

        self.files = []
        self.file_labels = []
        self.delete_buttons = []

        # Создать фрейм для отображения файлов
        self.files_frame = ctk.CTkFrame(self.root)
        self.files_frame.pack(pady=20)

        # Добавить кнопку для открытия файлового каталога
        self.open_button = ctk.CTkButton(self.root, text="Open Files", command=self.open_files)
        self.open_button.pack(pady=20)

    def open_files(self):
        # Открыть файловый каталог и получить список выбранных файлов
        files = ctk.filedialog.askopenfilenames()

        # Добавить названия файлов в фрейм для отображения файлов
        for index, file in enumerate(files):
            file_label = ctk.CTkLabel(self.files_frame, text=f"{index+1}. {file}")
            file_label.pack(side="top", padx=10, pady=5)

            # Добавить кнопку "delete" рядом с каждым названием файла
            delete_button = ctk.CTkButton(self.files_frame, text="Delete", command=lambda file=file: self.delete_file(file))
            delete_button.pack(side="right", padx=10)

            # Сохранить ссылки на метки и кнопки для дальнейшего использования
            self.files.append(file)
            self.file_labels.append(file_label)
            self.delete_buttons.append(delete_button)

    def delete_file(self, file):
        # Получить индекс удаляемого файла
        index = self.files.index(file)

        # Удалить метку и кнопку "delete"
        self.file_labels[index].destroy()
        self.delete_buttons[index].destroy()

        # Обновить список файлов и меток
        self.files.pop(index)
        self.file_labels.pop(index)
        self.delete_buttons.pop(index)

        # Перестроить оставшиеся файлы
        for i in range(len(self.files)):
            self.file_labels[i].configure(text=f"{i+1}. {self.files[i]}")


if __name__ == "__main__":
    app = App()
    app.root.mainloop()
