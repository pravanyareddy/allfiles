#include <iostream>
// Include Rpi-hw headers
#include <rpi-hw.hpp>
#include <rpi-hw/time.hpp>
#include <rpi-hw/keypad/matrix.hpp>

// Use Rpi-hw namespace
using namespace rpihw;

int
main( int argc, char *args[] ) {

   // Matrix keypad controller
   keypad::matrix dev( { 21, 10, 4 }, { 22, 14, 15, 17 } );

   // Main loop
   for ( ;; ) {

      // Check some keys state
      if ( dev.pressed(0) )
         std::cout << "You have pressed button 0!\n";

      if ( dev.released(2) )
         std::cout << "You have released button 2!\n";

      if ( dev.pressed(1) && dev.pressed(4) )
         std::cout << "You have pressed buttons 1 and 4!\n";

      // Wait some time
      time::msleep( 100 );
   }

   return 0;
}
