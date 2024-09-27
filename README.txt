  -- * en * --
* Brief description of the project *
ASCII-Imaging is a tool for converting a user image from jpg format to Ascii-art. It is the same image, but transmitted in text format without using graphic elements.

* Contact information and feedback *
Like most developers, including me, I am not isolated from society, which is very good in these times due to all these world conflicts. Here are all my social networks (You can write at any time, I am active and will try to answer everyone if you have such a need):
- Telegram: https://t.me/BimbaXdeV

* Instructions for use *
In the root folder of this project, you can find 2 folders necessary for work: "In" and "Out". One of them is responsible for feeding incoming images, and the second is for saving the output result of processing. Here is a step-by-step instruction on using the script:
- Put the desired image in the "In" folder;
- Open the system terminal (CMD command line) in Administrator mode (Optional, but you will lose some important secondary functionality that cannot be used automatically)
- Inside, navigate to the root folder of the project using the command "cd C:.../ASCII-Imaging/", and run the program using "python main.py";
- You have as many as 5 points at your disposal, let's analyze each of them separately:

  1. Converting a file to ASCII-art - after selecting, specify the name of the file you want to convert, after
     which the entire result will be saved along the path "C:.../ASCII-Imaging/Out/your_file.txt". Important notes:
    1. The input file must be specified immediately with its format at the end, for example: cute_cat.jpg, or frames.png;
    2. The file can have absolutely any name, but there are only 3 supported processing formats so far: .png, .jpg
       and .jpeg. The script will work with any image of these formats;
    3. You do not need to specify the output name, the resulting file will be written with the same name as the input file, only in the ".txt" format.

  2. Converting all files at once - a globalized method that can convert absolutely all files from the "In" folder in the root folder of the project. The method is useful for creating some mini-animations, or if you are too lazy to convert them all separately. Important notes:
    1. After selecting this item, you do not need to specify anything, the program will do everything for you;
    2. Do not worry about duplicating files with the same names - the old file will overwrite all the data from the new processing.

  3-4. Here everything is very simple: these methods are able to automatically clear folders from input and output files in
       the event that you do not need them, or you want to free up memory. Important notes:
    1. These methods will not work when running on behalf of the client. To perform absolutely all operations related to
       deleting anything - Administrator rights are required;
    2. The methods may not work correctly on other operating systems besides Windows 8-11;
    3. Please note that these methods delete absolutely all files from these folders, so if among the whole mass there is one or a couple of files you need - it is better not to use these methods for auto-deletion. In this situation,
       an ordinary file manager can help you, with which it is better to clear the folder from unnecessary files
       manually.

  5. This method is able to clear error logs, which are stored in the file along the path "C:.../ASCII-Imaging/Cache/". This file
     is needed to save and record all sorts of errors or exceptions in order to debug them in case they interfere with their
     use. Important notes:
    1. This file is not in the project folder by default, but is created after at least one error is output;
    2. Inside it stores not only the description of errors, but also the exact time of their output. Perhaps this will not play such a big role for use, but it can be useful for orientation in logs.

  6. Exiting the program, and its correct termination with the exit of the cycle. I do not know what else could be said about such a
     simple mechanics, so I think - that's all))

Enjoy using the program, and thank you very much for installing and testing it. Maybe it is not so deeply developed, maybe not very advanced optimized, but I tried to make it as convenient and intuitive as possible for each user. Good luck and success!

Release date: 02.07.2024 (Today its developer turned 16 years old)



  -- * ua * --
* Короткий опис проекту *
 ASCII-Imaging - це інструмент перетворення зображення користувача з jpg формату в Ascii-art. Він являє собою те саме зображення, проте передається в текстовому форматі без використання графічних елементів.

* Контактна інформація та зворотній зв'язок *
 Як і більшість розробників, включаючи мене - від суспільства я не ізольований, що дуже добре в даний час через всі ці світові конфлікти. Ось всі мої соціальні мережі (Ви можете написати у будь-який час, я активний і намагатимусь відповісти кожному, якщо у Вас є така потреба):
- Телеграм: https://t.me/BimbaXdeV

* Інструкція з використання *
У корінній папці даного проекту Ви можете знайти 2 необхідні для роботи папки: "In" та "Out". Одна з них відповідає за подачу вхідних зображень, а друга вже для збереження вихідного результату обробки. Ось покрокова інструкція щодо використання скрипта:
- Покладіть бажане зображення до папки "In";
- Відкрийте системний термінал (Командний рядок CMD) у режимі Адміністратора (Необов'язково, однак Ви втратите частину важливого другорядного функціоналу, який не вдасться використовувати автоматичним методом)
- Всередині проведіть шлях до кореневої папки проекту, використовуючи команду "cd C:.../ASCII-Imaging/", та запустіть програму за допомогою "python main.py";
- У Вашому розпорядженні цілих 5 пунктів, розберемо кожні з них окремо:

  1. Конвертація файлу в ASCII-art - після вибору вказуєте назву файлу, який Ви хочете конвертувати, після
     чого весь результат буде збережено шляхом "C:.../ASCII-Imaging/Out/your_file.txt". Важливі примітки:
    1. Вхідний файл необхідно вказувати одночасно з його форматом наприкінці, наприклад: cute_cat.jpg, чи frames.png;
    2. Файл може мати абсолютно будь-яку назву, але підтримуваний формат обробки поки-що тільки 3: .png, .jpg
       та .jpeg. Скрипт працюватиме з будь-яким зображенням цих форматів;
    3. Вказувати вихідну назву не потрібно, результат файлу буде записано з тією ж назвою, з якою було подано
       вхідний, лише у форматі ".txt".

  2. Конвертація всіх файлів разом - глобалізований метод, здатний конвертувати абсолютно всі файли з папки
     "In" у кореневій папці проекту. Метод корисний для створення яких-небудь міні-анімацій, або якщо Вам ліньки
     конвертувати їх усі окремо. Важливі примітки:
    1. Після вибору цього пункту Вам не потрібно нічого вказувати, програма все зробить за Вас;
    2. Не потрібно переживати щодо дублювання файлів з однаковими назвами - старий файл перезапише всі дані з
       нової обробки.

  3-4. Тут все дуже просто: ці методи здатні автоматично очистити папки від вхідних та вихідних файлів у
       Якщо Вам вони не будуть потрібні, або Ви захочете звільнити пам'ять. Важливі примітки:
    1. Дані методи не працюватимуть під час запуску від імені клієнта. Для здійснення абсолютно всіх операцій, пов'язаних
       з видаленням чогось – необхідні права Адміністратора;
    2. Методи можуть працювати некоректно інших операційних системах крім Windows 8-11;
    3. Зверніть увагу, що ці методи видаляють абсолютно всі файли з цих папок, тому якщо серед усієї маси лежить
       якийсь один або пара потрібних Вам файлів - краще не використовувати ці методи для видалення авто. У цій ситуації
       Вам допоможе звичайний файловий менеджер, за допомогою якого краще очистити папку від непотрібних Вам файлів
       вручну.

  5. Цей метод здатний очистити логи помилок, які зберігаються у файлі шляхом "C:.../ASCII-Imaging/Cache/". Цей файл
     потрібен для збереження та запису всіляких помилок або винятків, щоб налагодити їх у разі їх перешкод для
     їх використання. Важливі примітки:
    1. Цей файл відсутній у папці проекту за замовчуванням, однак створюється після виведення хоча б однієї помилки;
    2. Усередині він зберігає не тільки опис помилок, але також і точний час її виведення. Можливо, це не настільки
       сильно зіграє роль використання, проте може бути корисно для орієнтування по логах.

  6. Вихід із програми, та її коректне завершення з виходом циклу. Не знаю, що ще можна було б розповісти про
     таку звичайну механіку, тому, я думаю - на цьому все))

Приємного використання програми, і дякую за її встановлення і тестування. Може бути вона не настільки глибоко опрацьована, може бути не дуже оптимізована, проте я намагався зробити її максимально зручною та інтуїтивно зрозумілою для кожного користувача. Удачі та успіхів!

Дата випуску: 02.07.2024 (Сьогодні її розробнику виповнилося 16 років)



  -- * ru * --
* Краткое описание проекта *
 ASCII-Imaging - это инструмент преобразования пользовательского изображения из jpg формата в Ascii-art. Он представляет собой то же самое изображение, однако передающееся в текстовом формате без использования графических элементов.

* Контактная информация и обратная связь *
 Как и большинство разработчиков включая меня - от общества я не изолирован, что очень хорошо в нынешнее время из-за всех этих мировых конфликтов. Вот все мои социальные сети (Вы можете написать в любое время, я активный и постараюсь ответить каждому, если у Вас есть такая потребность):
- Телеграмм: https://t.me/BimbaXdeV

* Инструкция по использованию *
 В коренной папке данного проекта Вы можете обнаружить 2 необходимые для работы папки: "In" и "Out". Одна из них отвечает за подачу входящих изображений, а вторая уже для сохранения выходящего результата обработки. Вот пошаговая инструкция по использованию скрипта:
- Положите желаемое изображение в папку "In";
- Откройте системный терминал (Командную строку CMD) в режиме Администратора (Необязательно, однако Вы потеряете часть важного второстепенного функционала, который не получится использовать автоматическим методом)
- Внутри проведите путь до корневой папки проекта, используя команду "cd C:.../ASCII-Imaging/", и запустите программу при помощи "python main.py";
- В Вашем распоряжении целых 5 пунктов, разберём каждые из них по-отдельности:

  1. Конвертация файла в ASCII-art - после выбора указываете название файла, который Вы хотите конвертировать, после
     чего весь результат будет сохранён по пути "C:.../ASCII-Imaging/Out/your_file.txt". Важные примечания:
    1. Входной файл нужно указывать сразу же с его форматом в конце, к примеру: cute_cat.jpg, либо frames.png;
    2. Файл может иметь абсолютно любое название, но поддерживаемых формата обработки пока-что только 3: .png, .jpg
       и .jpeg. Скрипт будет работать с любым изображением этих форматов;
    3. Указывать выходное название не нужно, результат файла будет записан с тем же названием, с каким был подан
       входной, только уже в формате ".txt".

  2. Конвертация всех файлов разом - глобализированный метод, способный конвертировать абсолютно все файлы из папки
     "In" в корневой папке проекта. Метод полезен для создания каких-нибудь мини-анимаций, либо же если Вам лень
     конвертировать их все по-отдельности. Важные примечания:
    1. После выбора этого пункта Вам не нужно ничего указывать, программа всё сделает за Вас;
    2. Не нужно переживать на счёт дублирования файлов с одинаковыми названиями - старый файл перезапишет все данные с
       новой обработки.

  3-4. Тут всё предельно просто: эти методы способны автоматически очистить папки от входных и выходных файлов в
       случае, если Вам они не будут нужны, либо Вы захотите освободить память. Важные примечания:
    1. Данные методы не будут работать при запуске от имени клиента. Для совершения абсолютно всех операций, связанных
       с удалением чего-либо - необходимы права Администратора;
    2. Методы могут работать некорректно на других операционных системах помимо Windows 8-11;
    3. Обратите внимание, что эти методы удаляют абсолютно все файлы из этих папок, поэтому если среди всей массы лежит
       какой-то один или пара нужных Вам файлов - лучше не использовать эти методы для авто-удаления. В данной ситуации
       Вам сможет помочь обыкновенный файловый менеджер, с помощью которого лучше очистить папку от ненужных Вам файлов
       вручную.

  5. Этот метод способен очистить логи ошибок, которые хранятся в файле по пути "C:.../ASCII-Imaging/Cache/". Этот файл
     нужен для сохранения и записи всевозможных ошибок или исключений, дабы отладить их в случае их помех для
     их использованию. Важные примечания:
    1. Этот файл отсутствует в папке проекта по умолчанию, однако создаётся после выведения хотя-бы одной ошибки;
    2. Внутри он хранит не только описание ошибок, но так же и точное время её выведения. Возможно это не настолько
       сильно сыграет роль для использования, однако может быть полезно для ориентирования по логам.

  6. Выход из программы, и её корректное завершение с выходом цикла. Не знаю, что ещё можно было бы рассказать про
     столь обыкновенную механику, поэтому, я думаю - на этом всё))

Приятного использования программы, и спасибо большое за её установку и тестировку. Может быть она не настолько глубоко проработана, может быть не очень продвинуто оптимизирована, однако я старался сделать её максимально удобной и интуитивно понятной для каждого пользователя. Удачи и успехов!

Дата выпуска: 02.07.2024 (Сегодня её разработчику исполнилось 16 лет)