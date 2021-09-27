# Описание пакета gs_module

## Описание:
В этом пакете находятся классы для управления светодиодами

## Состав пакета:
Классы:
* BoardLedController
* ModuleLedController

## Описание классов:

### 1. BoardLedController
Класс для управления светодидами на борту

#### Инициализация:
BoardLedController(namespace = "") - namespace пространство имен в котором находится Пионер

#### Поля:
* __leds - list: std_msgs.msg.ColorRGBA
* __alive - rospy.ServiceProxy: gs_interfaces.srv.Live
* __led_service - rospy.ServiceProxy: gs_interfaces.srv.Led

#### Методы:
* changeColor(i,r,g,b) - зажигает конкретный светодиод, i - номер светодиода от 0 до 3, r - красный цвет от 0 до 255, g - зеленый цвет от 0 до 255, b - синий цвет от 0 до 255
* changeAllColor(r,g,b) - зажигает все светодиоды,  r - красный цвет от 0 до 255, g - зеленый цвет от 0 до 255, b - синий цвет от 0 до 255

#### Используемые сервисы:
* geoscan/alive (gs_interfaces/Live)
* geoscan/led/board/set (gs_interfaces/Led)

### 2. ModuleLedController
Класс для управления LED модулем

#### Инициализация:
ModuleLedController(namespace = "") - namespace пространство имен в котором находится Пионер

#### Поля:
* __leds - list: std_msgs.msg.ColorRGBA
* __alive - rospy.ServiceProxy: gs_interfaces.srv.Live
* __led_service - rospy.ServiceProxy: gs_interfaces.srv.Led

#### Методы:
* changeColor(i,r,g,b) - зажигает конкретный светодиод, i - номер светодиода от 0 до 24, r - красный цвет от 0 до 255, g - зеленый цвет от 0 до 255, b - синий цвет от 0 до 255
* changeAllColor(r,g,b) - зажигает все светодиоды, r - красный цвет от 0 до 255, g - зеленый цвет от 0 до 255, b - синий цвет от 0 до 255

#### Используемые сервисы:
* geoscan/alive (gs_interfaces/Live)
* geoscan/led/module/set (gs_interfaces/Led)

## Необходимые пакеты:
ROS:
* gs_interfaces
* gs_core
* std_msgs

## Примечание:
Все классы, кроме CargoController, могут быть использованы только при запущеной ноде ros_plaz_node.py из пакета gs_core