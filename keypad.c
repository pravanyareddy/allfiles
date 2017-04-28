#include <iostream>
#include <memory>
 
// Include Rpi-hw headers
#include <rpi-hw.hpp>
#include <rpi-hw/time.hpp>
#include <rpi-hw/keypad/matrix.hpp>
 
// Use the Rpi-hw namespace
using namespace rpihw;
 
/*
      (14, 15, 18, 23)   colums = 4
            ||||
   ----------------------
   | (1)  (2)  (3)  (A) |
   |                    |
   | (4)  (5)  (6)  (B) |
   |                    |
   | (7)  (8)  (9)  (C) |
   |                    |
   | (*)  (0)  (#)  (D) |
   ----------------------
            ||||
       (24, 25, 8, 7)  rows = 4
*/
 
/** The class of my application **/
class MyApp {
 
public:
 
    // Define the keymap
    std::vector< uint8_t > keymap = {
 
        '1', '2', '3', 'A',
        '4', '5', '6', 'B',
        '7', '8', '9', 'C',
        '*', '0', '#', 'D'
    };
 
    /** Constructor method **/
    MyApp() : m_keypad( new keypad::matrix( { 14, 15, 18, 23 }, { 24, 25, 8, 7 }, keymap ) ) {
 
        keypad::T_EventListener listener = std::bind( &MyApp::eventListener, this, std::placeholders::_1 );
 
        // Add the keypad event listener
        m_keypad->addEventListener( listener );
    }
 
    /** Destructor method **/
    ~MyApp() {}
 
    /** A simple keypad event listener **/
    void eventListener( keypad::base &dev ) {
 
        const std::vector< uint8_t > &keystate = dev.keyState();
 
        for ( uint8_t c : keystate )
            std::cout << (char) c << std::flush;
    }
 
    /** Main loop **/
    void run() {
 
        for ( ;; ) {
 
            /* ... */
        }
    }
 
private:
 
    //! The keypad instance.
    std::unique_ptr< keypad::matrix > m_keypad;
};
 
 
int
main( int argc, char *args[] ) {
 
    MyApp app;
 
    app.run();
 
    return 0;
}
