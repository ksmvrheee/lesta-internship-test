## Здравствуйте.

## Задание 1

В данном мне примере реализован, пожалуй, наиболее оптимальный алгоритм проверки на чётность. Алгоритм же, который я написал, стоит использовать разве что ради демонстрации. Суть его такова: мы проверяем, присутствует ли дробная часть у результата деления входного числа на два. Если да, то оно нечётное. Эту проверку позволяет осуществить метод .is_integer() встроенного класса/типа float. Для осуществления этой проверки необходимо сначала создать float-объект из результата деления числа на два, а потом вызвать у него этот метод.
В изначальном примере сразу же проверяется наличие остатка при делении на два исходного числа. Это более прямой и логичный путь.

## Задание 2

В первом случае циклический буфер FIFO я реализовал без использования каких-либо библиотек. Был реализован класс, который получает в конструктор лишь один аргумент — размер/ёмкость буфера. Внутри класса сразу же создаётся список из None-значений (предполагается, что данные не должны быть None) и три переменные: для размера хранимых элементов, а также для индексов "головы" и "хвоста" буфера. Кроме конструктора, реализованы ещё три метода: для добавления элемента в конец буфера, для удаления/получения верхнего элемента из буфера, а также для проверки текущего состояния структуры. Также реализованы магические методы __str__ и __bool__ для более простого взаимодействия с экземплярами класса внутри кода.
Второй случай — демонстрация реализации такой структуры данных через встроенный класс collections.deque. Получается практически то же самое. В конструктор можно передать заготовку массива и аргумент maxlen, определяющий максимальную длину буфера.
Скорее всего, второй способ обеспечит более высокую скорость выполнения, однако первый куда проще для понимания и использования.

## Задание 3

Я реализовал функцию быстрой сортировки на базе quicksort, использующую рекурсивный алгоритм и разделяющую данный ей массив на несколько других (меньше, больше и равны первому элементу), однако обходящуюся без злоупотребления памятью.

## Спасибо за внимание.