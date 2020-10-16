# Описание пакета gs_module

## Описание:
В этом пакете находятся классы для управления светодиодами

## Состав пакета:
Классы:
* BoardLedController
* ModuleLedController
* CargoController

## Описание классов:

### 1. BoardLedController
Класс для управления светодидами на борту

#### Инициализация:
Без параметров

#### Поля:
* __leds - list: gs_interfaces.msg.RGBgs
* __alive - rospy.ServiceProxy: gs_interfaces.srv.Live
* __led_service - rospy.ServiceProxy: gs_interfaces.srv.Led

#### Методы:
* changeColor(i,r,g,b) - зажигает конкретный светодиод, i - номер светодиода, r - красный цвет от 0 или 1, g - зеленый цвет 0 или 1, b - синий цвет 0 или 1
* changeAllColor(r,g,b) - зажигает все светодиоды,  r - красный цвет 0 или 1, g - зеленый цвет 0 или 1, b - синий цвет 0 или 1

#### Используемые сервисы:
* geoscan/alive (gs_interfaces/Live)
* geoscan/led/board/control_service (gs_interfaces/Led)

### 2. ModuleLedController
Класс для управления LED модулем

#### Инициализация:
Без параметров

#### Поля:
* __leds - list: gs_interfaces.msg.RGBgs
* __alive - rospy.ServiceProxy: gs_interfaces.srv.Live
* __led_service - rospy.ServiceProxy: gs_interfaces.srv.Led

#### Методы:
* changeColor(i,r,g,b) - зажигает конкретный светодиод, i - номер светодиода, r - красный цвет 0 или 1, g - зеленый цвет 0 или 1, b - синий цвет 0 или 1
* changeAllColor(r,g,b) - зажигает все светодиоды,  r - красный цвет 0 или 1, g - зеленый цвет 0 или 1, b - синий цвет 0 или 1

#### Используемые сервисы:
* geoscan/alive (gs_interfaces/Live)
* geoscan/led/module/control_service (gs_interfaces/Led)

### 3. CargoController
Класс для управления модулем магнитного захвата

#### Инициализация:
Без параметров

#### Поля:
* __alive - rospy.ServiceProxy: gs_interfaces.srv.Live
* __cargo_service - rospy.ServiceProxy: gs_interfaces.srv.Cargo

#### Методы:
* set() - включить магнитный захват
* reset() -выключить магнитный захват

#### Используемые сервисы:
* geoscan/alive (gs_interfaces/Live)
* geoscan/cargo (gs_interfaces/Cargo)

## Необходимые пакеты:
ROS:
* gs_interfaces
* gs_core
* std_msgs

## Примечание:
Все классы в данном пакете могут быть использованы только при запущеной ноде ros_serial_node.py из пакета gs_core