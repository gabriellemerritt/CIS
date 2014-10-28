#include <pebble.h>


#define Symbol 0
#define LastPrice 1
#define ChangePercent 2

#define NUM_MENU_SECTIONS 3 

static Window *window;
static TextLayer *text_layer;
static TextLayer *s_stock_layer;
static GFont s_stock_font;
// pebble made simple menu
static SimpleMenuLayer *stock_menu_layer; 
// creating 3 sections on the menu so we can look at 3 different stocks
static SimpleMenuSection menu_sections[3]; 
static SimpleMenuItem first_stock[1]; 
static SimpleMenuItem second_stock[1]; 
static SimpleMenuItem third_stock[1]; 

static void menu_select_callback(int index, void *context) {
  s_stock_layer = text_layer_create(GRect(0, 130, 144, 25));
  text_layer_set_background_color(s_stock_layer, GColorClear);
  text_layer_set_text_color(s_stock_layer, GColorWhite);
  text_layer_set_text_alignment(s_stock_layer, GTextAlignmentCenter);
  text_layer_set_text(s_stock_layer, "Loading...");
  
  // Create second custom font, apply it and add to Window
  s_stock_font = fonts_load_custom_font(resource_get_handle(RESOURCE_ID_FONT_CNL_10));
  text_layer_set_font(s_stock_layer, s_stock_font);
  layer_add_child(window_get_root_layer(window), text_layer_get_layer(s_stock_layer));
  
  DictionaryIterator *iter;
  app_message_outbox_begin(&iter);
  dict_write_cstring(iter, 0, "AAPL");
  app_message_outbox_send();
  // Mark the layer to be updated
  layer_mark_dirty(simple_menu_layer_get_layer(stock_menu_layer));
}
static void window_load(Window *window) {
  // We'll have to load the icon before we can use it
  // menu_icon_image = gbitmap_create_with_resource(RESOURCE_ID_IMAGE_MENU_ICON_1);

  // defining the menu items and their specific call backs 
  first_stock[0] = (SimpleMenuItem){
    .title = "Apple",
    .callback = menu_select_callback,
  };

  //  second section
  second_stock[0] = (SimpleMenuItem){
    .title = "Microsoft",
    // You can use different callbacks for your menu items
    .callback = menu_select_callback,
  };
  // third section 
  third_stock[0] = (SimpleMenuItem){
    .title = "Google",
    .callback = menu_select_callback,
    // .icon = menu_icon_image,
  };

  // Link menu items to menu sections
  menu_sections[0] = (SimpleMenuSection){
    .items = first_stock,
    .num_items = 1,
    .title = "Apple Corp"

  };
  menu_sections[1] = (SimpleMenuSection){
    .items = second_stock,
    .num_items = 1,
    .title = "Microsoft"
  };
  menu_sections[2] = (SimpleMenuSection){
    .items = third_stock,
    .num_items = 1, // all the sections only have one item which calls and requests stock prices
    .title = "Google"
  };

  

  // Now we prepare to initialize the simple menu layer
  // We need the bounds to specify the simple menu layer's viewport size
  // In this case, it'll be the same as the window's
  Layer *window_layer = window_get_root_layer(window);
  GRect bounds = layer_get_frame(window_layer);

  // Initialize the simple menu layer
 stock_menu_layer = simple_menu_layer_create(bounds, window, menu_sections, NUM_MENU_SECTIONS, NULL);

  // Add it to the window for display
  layer_add_child(window_layer, simple_menu_layer_get_layer(stock_menu_layer));
}

static void inbox_received_callback(DictionaryIterator *iterator, void *context) {
  // Store incoming information
  static char symbol_buffer[32];
  static char price_buffer[32];
  static char changepercent_buffer[32];
  static char stock_layer_buffer[32];
  
  // Read first item
  Tuple *t = dict_read_first(iterator);

  // For all items
  while(t != NULL) {
    // Which key was received
    switch(t->key) {
    // determining if dic entry was symbol , last price or change of percentage 
    case Symbol:
      snprintf(symbol_buffer, sizeof(symbol_buffer), "%s", t->value->cstring);
      break;
    case LastPrice:
      snprintf(price_buffer, sizeof(price_buffer), "%d", (int)t->value->int32);
      break;
    case ChangePercent:
      snprintf(changepercent_buffer, sizeof(changepercent_buffer),"%d%%",(int)t->value->int32);
      break;
    default:
      APP_LOG(APP_LOG_LEVEL_ERROR, "Key %d not recognized!", (int)t->key);
      break;
    }

    // Look for next item
    t = dict_read_next(iterator);
  }
  
  // put stock info on the text layer created in the menu call back function 
  snprintf(stock_layer_buffer, sizeof(stock_layer_buffer), "%s, %s, %s", symbol_buffer, price_buffer,changepercent_buffer);
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
static void window_unload(Window *window) {
  text_layer_destroy(text_layer);
}

static void init(void) {
  //init function creates and handles the main window 
  window = window_create();
  window_set_window_handlers(window, (WindowHandlers) {
    .load = window_load,
    .unload = window_unload,
  });
  const bool animated = true;

 // animates transitions between windows
  window_stack_push(window, animated);
  app_message_register_inbox_received(inbox_received_callback);
  app_message_register_inbox_dropped(inbox_dropped_callback);
  app_message_register_outbox_failed(outbox_failed_callback);
  app_message_register_outbox_sent(outbox_sent_callback);
  
  // Open AppMessage
  app_message_open(app_message_inbox_size_maximum(), app_message_outbox_size_maximum());
}

static void deinit(void) {
  //close out of main window
  window_destroy(window);

}

int main(void) {
  init();
  app_event_loop();
  deinit();
}