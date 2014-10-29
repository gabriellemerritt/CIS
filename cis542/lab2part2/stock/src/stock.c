#include <pebble.h>
  
// This watch app shows price and percent change of Stock , Clicking the select toggles between Apple and Google Stocks
#define Symbol 0
#define LastPrice 1
#define ChangePercent 2

#define NUM_MENU_SECTIONS 3 

static Window *window;
static TextLayer *text_layer;
static TextLayer *s_stock_layer;
static GFont s_stock_font; // font which stocks appear 
static BitmapLayer *s_slayer; // image bitmap layer for stock arrow
static GBitmap *s_sbitmap; //  image bitmap for stock arrow
static BitmapLayer *s_background_layer; // background bitmap layer
static GBitmap *s_background_bitmap;

static char stock_layer_buffer[32];


static void main_window_load(Window *window) {
s_background_bitmap = gbitmap_create_with_resource(RESOURCE_ID_IMAGE_BACKGROUND);
s_background_layer = bitmap_layer_create(GRect(0, 0, 144, 168));
bitmap_layer_set_bitmap(s_background_layer, s_background_bitmap);
layer_add_child(window_get_root_layer(window), bitmap_layer_get_layer(s_background_layer));

s_stock_layer = text_layer_create(GRect(0, 100, 144, 168));
text_layer_set_background_color(s_stock_layer, GColorClear);
text_layer_set_text_color(s_stock_layer, GColorWhite);
text_layer_set_text_alignment(s_stock_layer, GTextAlignmentCenter);
text_layer_set_text(s_stock_layer, "Loading...");

  // Create second custom font, apply it and add to Window
s_stock_font = fonts_load_custom_font(resource_get_handle(RESOURCE_ID_FONT_CNL_20));
text_layer_set_font(s_stock_layer, s_stock_font);
layer_add_child(window_get_root_layer(window), text_layer_get_layer(s_stock_layer));

// writing the symbol for appl to the dict so javascript can use it 

}

static void main_window_unload(Window *window) {

  //Destroy GBitmap
  gbitmap_destroy(s_background_bitmap);

  //Destroy BitmapLayer
  bitmap_layer_destroy(s_background_layer);
  
  // Destroy TextLayer
  text_layer_destroy(text_layer);
  
  // Destroy weather elements
  text_layer_destroy(s_stock_layer);
  fonts_unload_custom_font(s_stock_font);

  // destroy weather image 
  bitmap_layer_destroy(s_slayer); 
  gbitmap_destroy(s_sbitmap);
}

static void select_click_handler(ClickRecognizerRef recognizer, void *context) {
 
  APP_LOG(APP_LOG_LEVEL_INFO, "started select_click_handler");
  // initializes pointer
  DictionaryIterator *iter; 
  // shows where the message is stored
  app_message_outbox_begin(&iter); 
  // just sending random key and pair value since the toggling is done in the javascript 
  dict_write_uint8(iter, 100, 100);
  // sends the message to js letting it know it has a message
  app_message_outbox_send();
  APP_LOG(APP_LOG_LEVEL_INFO, "Sent write to app message"); 
  // setting the text layer 
  text_layer_set_text(s_stock_layer, stock_layer_buffer);
  APP_LOG(APP_LOG_LEVEL_INFO, "exited select_click_handler without seg fault");


}
static void config_provider(void *context) {
    // when clicking select go to the select handler 
     window_single_click_subscribe(BUTTON_ID_SELECT, select_click_handler);
 }

static void inbox_received_callback(DictionaryIterator *iterator, void *context) {
  APP_LOG(APP_LOG_LEVEL_INFO, "Pebble in inbox call back");
  // Store incoming information
  static char symbol_buffer[32];
  static char price_buffer[64];
  static char changepercent_buffer[64];
  static char stock_layer_buffer[64];
  // just a float number to simplify converting 
  float change_percent = 0; 
  float req_price = 0; 
  
  // Read first item
  Tuple *t = dict_read_first(iterator);

  // For all items
  while(t != NULL) {
    // Which key was received
    switch(t->key) {
    // determining if dic entry was symbol , last price or change of percentage 
    case Symbol:
      // printing and saving the value at the key to a buffer
      snprintf(symbol_buffer, sizeof(symbol_buffer), "%s", t->value->cstring);
      break;
    case LastPrice:
      req_price = (int)t->value->int32/100.00; 
      snprintf(price_buffer, sizeof(price_buffer), "%g", req_price);
      break;
    case ChangePercent:
      change_percent = ((int)t->value->int32)/100.00; 
      snprintf(changepercent_buffer, sizeof(changepercent_buffer),"%g%%",change_percent);
      if(s_sbitmap)
      {
          // clearing the previous arrow image 
          gbitmap_destroy(s_sbitmap);
          bitmap_layer_destroy(s_slayer);
      }
      // matching up up or down arrow with change of percent in stock 
      if (change_percent < 0) // down arrow
      {

        s_sbitmap = gbitmap_create_with_resource(RESOURCE_ID_IMAGE_DOWN);
        s_slayer = bitmap_layer_create(GRect(20, 30, 105, 50));
        bitmap_layer_set_bitmap(s_slayer, s_sbitmap);
        layer_add_child(window_get_root_layer(window),bitmap_layer_get_layer(s_slayer));
  
      }
      else { // uparrow 
        s_sbitmap = gbitmap_create_with_resource(RESOURCE_ID_IMAGE_UP);
        s_slayer = bitmap_layer_create(GRect(20, 30, 105, 50));
        bitmap_layer_set_bitmap(s_slayer, s_sbitmap);
        layer_add_child(window_get_root_layer(window),bitmap_layer_get_layer(s_slayer));
        APP_LOG(APP_LOG_LEVEL_INFO, "Finished loading arrow");
  

      }
      break;
    default:
      APP_LOG(APP_LOG_LEVEL_ERROR, "Key %d not recognized!", (int)t->key);
      break;
    }

    // Look for next item
    t = dict_read_next(iterator);
  }
  
  // put stock info on the text layer created in the menu call back function 
  snprintf(stock_layer_buffer, sizeof(stock_layer_buffer), "%s \n $%s \n%s", symbol_buffer, price_buffer,changepercent_buffer);
  text_layer_set_text(s_stock_layer, stock_layer_buffer);
}

static void inbox_dropped_callback(AppMessageResult reason, void *context) {
  APP_LOG(APP_LOG_LEVEL_ERROR, "Message dropped!");
}

static void outbox_failed_callback(DictionaryIterator *iterator, AppMessageResult reason, void *context) {
  APP_LOG(APP_LOG_LEVEL_ERROR, "Outbox send failed!");
}

static void outbox_sent_callback(DictionaryIterator *iterator, void *context) {

  APP_LOG(APP_LOG_LEVEL_INFO, "Outbox send success!");
}


static void init() {
  // Create main Window element and assign to pointer
  window = window_create();
  // associate click with the current window 

  // Set handlers to manage the elements inside the Window
  window_set_window_handlers(window, (WindowHandlers) {
    .load = main_window_load,
    .unload = main_window_unload
  });

  // Show the Window on the watch, with animated=true
  window_stack_push(window, true);
  
  window_set_click_config_provider(window, config_provider);
  //tick_timer_service_subscribe(MINUTE_UNIT, tick_handler);


  // Register callbacks
  app_message_register_inbox_received(inbox_received_callback);
  app_message_register_inbox_dropped(inbox_dropped_callback);
  app_message_register_outbox_failed(outbox_failed_callback);
  app_message_register_outbox_sent(outbox_sent_callback);
  
  // Open AppMessage
  app_message_open(app_message_inbox_size_maximum(), app_message_outbox_size_maximum());
}

static void deinit() {
  // Destroy Window
  window_destroy(window);

}

int main(void) {
  init();
  app_event_loop();
  deinit();
}
