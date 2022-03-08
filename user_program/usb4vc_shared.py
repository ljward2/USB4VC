RPI_APP_VERSION_TUPLE = (0, 0, 6)

code_name_to_value_lookup = {
	'KEY_RESERVED':(0, 'kb_key'),
	'KEY_ESC':(1, 'kb_key'),
	'KEY_1':(2, 'kb_key'),
	'KEY_2':(3, 'kb_key'),
	'KEY_3':(4, 'kb_key'),
	'KEY_4':(5, 'kb_key'),
	'KEY_5':(6, 'kb_key'),
	'KEY_6':(7, 'kb_key'),
	'KEY_7':(8, 'kb_key'),
	'KEY_8':(9, 'kb_key'),
	'KEY_9':(10, 'kb_key'),
	'KEY_0':(11, 'kb_key'),
	'KEY_MINUS':(12, 'kb_key'),
	'KEY_EQUAL':(13, 'kb_key'),
	'KEY_BACKSPACE':(14, 'kb_key'),
	'KEY_TAB':(15, 'kb_key'),
	'KEY_Q':(16, 'kb_key'),
	'KEY_W':(17, 'kb_key'),
	'KEY_E':(18, 'kb_key'),
	'KEY_R':(19, 'kb_key'),
	'KEY_T':(20, 'kb_key'),
	'KEY_Y':(21, 'kb_key'),
	'KEY_U':(22, 'kb_key'),
	'KEY_I':(23, 'kb_key'),
	'KEY_O':(24, 'kb_key'),
	'KEY_P':(25, 'kb_key'),
	'KEY_LEFTBRACE':(26, 'kb_key'),
	'KEY_RIGHTBRACE':(27, 'kb_key'),
	'KEY_ENTER':(28, 'kb_key'),
	'KEY_LEFTCTRL':(29, 'kb_key'),
	'KEY_A':(30, 'kb_key'),
	'KEY_S':(31, 'kb_key'),
	'KEY_D':(32, 'kb_key'),
	'KEY_F':(33, 'kb_key'),
	'KEY_G':(34, 'kb_key'),
	'KEY_H':(35, 'kb_key'),
	'KEY_J':(36, 'kb_key'),
	'KEY_K':(37, 'kb_key'),
	'KEY_L':(38, 'kb_key'),
	'KEY_SEMICOLON':(39, 'kb_key'),
	'KEY_APOSTROPHE':(40, 'kb_key'),
	'KEY_GRAVE':(41, 'kb_key'),
	'KEY_LEFTSHIFT':(42, 'kb_key'),
	'KEY_BACKSLASH':(43, 'kb_key'),
	'KEY_Z':(44, 'kb_key'),
	'KEY_X':(45, 'kb_key'),
	'KEY_C':(46, 'kb_key'),
	'KEY_V':(47, 'kb_key'),
	'KEY_B':(48, 'kb_key'),
	'KEY_N':(49, 'kb_key'),
	'KEY_M':(50, 'kb_key'),
	'KEY_COMMA':(51, 'kb_key'),
	'KEY_DOT':(52, 'kb_key'),
	'KEY_SLASH':(53, 'kb_key'),
	'KEY_RIGHTSHIFT':(54, 'kb_key'),
	'KEY_KPASTERISK':(55, 'kb_key'),
	'KEY_LEFTALT':(56, 'kb_key'),
	'KEY_SPACE':(57, 'kb_key'),
	'KEY_CAPSLOCK':(58, 'kb_key'),
	'KEY_F1':(59, 'kb_key'),
	'KEY_F2':(60, 'kb_key'),
	'KEY_F3':(61, 'kb_key'),
	'KEY_F4':(62, 'kb_key'),
	'KEY_F5':(63, 'kb_key'),
	'KEY_F6':(64, 'kb_key'),
	'KEY_F7':(65, 'kb_key'),
	'KEY_F8':(66, 'kb_key'),
	'KEY_F9':(67, 'kb_key'),
	'KEY_F10':(68, 'kb_key'),
	'KEY_NUMLOCK':(69, 'kb_key'),
	'KEY_SCROLLLOCK':(70, 'kb_key'),
	'KEY_KP7':(71, 'kb_key'),
	'KEY_KP8':(72, 'kb_key'),
	'KEY_KP9':(73, 'kb_key'),
	'KEY_KPMINUS':(74, 'kb_key'),
	'KEY_KP4':(75, 'kb_key'),
	'KEY_KP5':(76, 'kb_key'),
	'KEY_KP6':(77, 'kb_key'),
	'KEY_KPPLUS':(78, 'kb_key'),
	'KEY_KP1':(79, 'kb_key'),
	'KEY_KP2':(80, 'kb_key'),
	'KEY_KP3':(81, 'kb_key'),
	'KEY_KP0':(82, 'kb_key'),
	'KEY_KPDOT':(83, 'kb_key'),
	'KEY_ZENKAKUHANKAKU':(85, 'kb_key'),
	'KEY_102ND':(86, 'kb_key'),
	'KEY_F11':(87, 'kb_key'),
	'KEY_F12':(88, 'kb_key'),
	'KEY_RO':(89, 'kb_key'),
	'KEY_KATAKANA':(90, 'kb_key'),
	'KEY_HIRAGANA':(91, 'kb_key'),
	'KEY_HENKAN':(92, 'kb_key'),
	'KEY_KATAKANAHIRAGANA':(93, 'kb_key'),
	'KEY_MUHENKAN':(94, 'kb_key'),
	'KEY_KPJPCOMMA':(95, 'kb_key'),
	'KEY_KPENTER':(96, 'kb_key'),
	'KEY_RIGHTCTRL':(97, 'kb_key'),
	'KEY_KPSLASH':(98, 'kb_key'),
	'KEY_SYSRQ':(99, 'kb_key'),
	'KEY_RIGHTALT':(100, 'kb_key'),
	'KEY_LINEFEED':(101, 'kb_key'),
	'KEY_HOME':(102, 'kb_key'),
	'KEY_UP':(103, 'kb_key'),
	'KEY_PAGEUP':(104, 'kb_key'),
	'KEY_LEFT':(105, 'kb_key'),
	'KEY_RIGHT':(106, 'kb_key'),
	'KEY_END':(107, 'kb_key'),
	'KEY_DOWN':(108, 'kb_key'),
	'KEY_PAGEDOWN':(109, 'kb_key'),
	'KEY_INSERT':(110, 'kb_key'),
	'KEY_DELETE':(111, 'kb_key'),
	'KEY_MACRO':(112, 'kb_key'),
	'KEY_MUTE':(113, 'kb_key'),
	'KEY_VOLUMEDOWN':(114, 'kb_key'),
	'KEY_VOLUMEUP':(115, 'kb_key'),
	'KEY_POWER':(116, 'kb_key'),
	'KEY_KPEQUAL':(117, 'kb_key'),
	'KEY_KPPLUSMINUS':(118, 'kb_key'),
	'KEY_PAUSE':(119, 'kb_key'),
	'KEY_SCALE':(120, 'kb_key'),
	'KEY_KPCOMMA':(121, 'kb_key'),
	'KEY_HANGEUL':(122, 'kb_key'),
	'KEY_HANGUEL':(122, 'kb_key'),
	'KEY_HANJA':(123, 'kb_key'),
	'KEY_YEN':(124, 'kb_key'),
	'KEY_LEFTMETA':(125, 'kb_key'),
	'KEY_RIGHTMETA':(126, 'kb_key'),
	'KEY_COMPOSE':(127, 'kb_key'),
	'KEY_STOP':(128, 'kb_key'),
	'KEY_AGAIN':(129, 'kb_key'),
	'KEY_PROPS':(130, 'kb_key'),
	'KEY_UNDO':(131, 'kb_key'),
	'KEY_FRONT':(132, 'kb_key'),
	'KEY_COPY':(133, 'kb_key'),
	'KEY_OPEN':(134, 'kb_key'),
	'KEY_PASTE':(135, 'kb_key'),
	'KEY_FIND':(136, 'kb_key'),
	'KEY_CUT':(137, 'kb_key'),
	'KEY_HELP':(138, 'kb_key'),
	'KEY_MENU':(139, 'kb_key'),
	'KEY_CALC':(140, 'kb_key'),
	'KEY_SETUP':(141, 'kb_key'),
	'KEY_SLEEP':(142, 'kb_key'),
	'KEY_WAKEUP':(143, 'kb_key'),
	'KEY_FILE':(144, 'kb_key'),
	'KEY_SENDFILE':(145, 'kb_key'),
	'KEY_DELETEFILE':(146, 'kb_key'),
	'KEY_XFER':(147, 'kb_key'),
	'KEY_PROG1':(148, 'kb_key'),
	'KEY_PROG2':(149, 'kb_key'),
	'KEY_WWW':(150, 'kb_key'),
	'KEY_MSDOS':(151, 'kb_key'),
	'KEY_COFFEE':(152, 'kb_key'),
	'KEY_SCREENLOCK':(152, 'kb_key'),
	'KEY_ROTATE_DISPLAY':(153, 'kb_key'),
	'KEY_DIRECTION':(153, 'kb_key'),
	'KEY_CYCLEWINDOWS':(154, 'kb_key'),
	'KEY_MAIL':(155, 'kb_key'),
	'KEY_BOOKMARKS':(156, 'kb_key'),
	'KEY_COMPUTER':(157, 'kb_key'),
	'KEY_BACK':(158, 'kb_key'),
	'KEY_FORWARD':(159, 'kb_key'),
	'KEY_CLOSECD':(160, 'kb_key'),
	'KEY_EJECTCD':(161, 'kb_key'),
	'KEY_EJECTCLOSECD':(162, 'kb_key'),
	'KEY_NEXTSONG':(163, 'kb_key'),
	'KEY_PLAYPAUSE':(164, 'kb_key'),
	'KEY_PREVIOUSSONG':(165, 'kb_key'),
	'KEY_STOPCD':(166, 'kb_key'),
	'KEY_RECORD':(167, 'kb_key'),
	'KEY_REWIND':(168, 'kb_key'),
	'KEY_PHONE':(169, 'kb_key'),
	'KEY_ISO':(170, 'kb_key'),
	'KEY_CONFIG':(171, 'kb_key'),
	'KEY_HOMEPAGE':(172, 'kb_key'),
	'KEY_REFRESH':(173, 'kb_key'),
	'KEY_EXIT':(174, 'kb_key'),
	'KEY_MOVE':(175, 'kb_key'),
	'KEY_EDIT':(176, 'kb_key'),
	'KEY_SCROLLUP':(177, 'kb_key'),
	'KEY_SCROLLDOWN':(178, 'kb_key'),
	'KEY_KPLEFTPAREN':(179, 'kb_key'),
	'KEY_KPRIGHTPAREN':(180, 'kb_key'),
	'KEY_NEW':(181, 'kb_key'),
	'KEY_REDO':(182, 'kb_key'),
	'KEY_F13':(183, 'kb_key'),
	'KEY_F14':(184, 'kb_key'),
	'KEY_F15':(185, 'kb_key'),
	'KEY_F16':(186, 'kb_key'),
	'KEY_F17':(187, 'kb_key'),
	'KEY_F18':(188, 'kb_key'),
	'KEY_F19':(189, 'kb_key'),
	'KEY_F20':(190, 'kb_key'),
	'KEY_F21':(191, 'kb_key'),
	'KEY_F22':(192, 'kb_key'),
	'KEY_F23':(193, 'kb_key'),
	'KEY_F24':(194, 'kb_key'),
	# --------------------
	'BTN_GAMEPAD':(0x130, 'usb_gp_btn'),
	'BTN_SOUTH':(0x130, 'usb_gp_btn'),
	'BTN_A':(0x130, 'usb_gp_btn'),
	'BTN_EAST':(0x131, 'usb_gp_btn'),
	'BTN_B':(0x131, 'usb_gp_btn'),
	'BTN_C':(0x132, 'usb_gp_btn'),
	'BTN_NORTH':(0x133, 'usb_gp_btn'),
	'BTN_X':(0x133, 'usb_gp_btn'),
	'BTN_WEST':(0x134, 'usb_gp_btn'),
	'BTN_Y':(0x134, 'usb_gp_btn'),
	'BTN_Z':(0x135, 'usb_gp_btn'),
	'BTN_TL':(0x136, 'usb_gp_btn'),
	'BTN_TR':(0x137, 'usb_gp_btn'),
	'BTN_TL2':(0x138, 'usb_gp_btn'),
	'BTN_TR2':(0x139, 'usb_gp_btn'),
	'BTN_SELECT':(0x13a, 'usb_gp_btn'),
	'BTN_START':(0x13b, 'usb_gp_btn'),
	'BTN_MODE':(0x13c, 'usb_gp_btn'),
	'BTN_THUMBL':(0x13d, 'usb_gp_btn'),
	'BTN_THUMBR':(0x13e, 'usb_gp_btn'),
	# --------------------
	'ABS_X':(0x00, 'usb_abs_axis'),
	'ABS_Y':(0x01, 'usb_abs_axis'),
	'ABS_Z':(0x02, 'usb_abs_axis'),
	'ABS_RX':(0x03, 'usb_abs_axis'),
	'ABS_RY':(0x04, 'usb_abs_axis'),
	'ABS_RZ':(0x05, 'usb_abs_axis'),
	'ABS_THROTTLE':(0x06, 'usb_abs_axis'),
	'ABS_RUDDER':(0x07, 'usb_abs_axis'),
	'ABS_WHEEL':(0x08, 'usb_abs_axis'),
	'ABS_GAS':(0x09, 'usb_abs_axis'),
	'ABS_BRAKE':(0x0a, 'usb_abs_axis'),
	'ABS_HAT0X':(0x10, 'usb_abs_axis'),
	'ABS_HAT0Y':(0x11, 'usb_abs_axis'),
	'ABS_HAT1X':(0x12, 'usb_abs_axis'),
	'ABS_HAT1Y':(0x13, 'usb_abs_axis'),
	'ABS_HAT2X':(0x14, 'usb_abs_axis'),
	'ABS_HAT2Y':(0x15, 'usb_abs_axis'),
	'ABS_HAT3X':(0x16, 'usb_abs_axis'),
	'ABS_HAT3Y':(0x17, 'usb_abs_axis'),
	# --------------------
	'BTN_MOUSE':(0x110, 'mouse_btn'),
	'BTN_LEFT':(0x110, 'mouse_btn'),
	'BTN_RIGHT':(0x111, 'mouse_btn'),
	'BTN_MIDDLE':(0x112, 'mouse_btn'),
	'BTN_SIDE':(0x113, 'mouse_btn'),
	'BTN_EXTRA':(0x114, 'mouse_btn'),
	'BTN_FORWARD':(0x115, 'mouse_btn'),
	'BTN_BACK':(0x116, 'mouse_btn'),
	'BTN_TASK':(0x117, 'mouse_btn'),
	# --------------------
	'REL_X':(0x00, 'usb_rel_axis'),
	'REL_Y':(0x01, 'usb_rel_axis'),
	'REL_Z':(0x02, 'usb_rel_axis'),
	'REL_RX':(0x03, 'usb_rel_axis'),
	'REL_RY':(0x04, 'usb_rel_axis'),
	'REL_RZ':(0x05, 'usb_rel_axis'),
	'REL_HWHEEL':(0x06, 'usb_rel_axis'),
	'REL_DIAL':(0x07, 'usb_rel_axis'),
	'REL_WHEEL':(0x08, 'usb_rel_axis'),
	'REL_MISC':(0x09, 'usb_rel_axis'),
	# --------------------
	'IBM_GGP_BTN_1':('IBM_GGP_BTN_1', 'ibm_ggp_btn'),
	'IBM_GGP_BTN_2':('IBM_GGP_BTN_2', 'ibm_ggp_btn'),
	'IBM_GGP_BTN_3':('IBM_GGP_BTN_3', 'ibm_ggp_btn'),
	'IBM_GGP_BTN_4':('IBM_GGP_BTN_4', 'ibm_ggp_btn'),
	# --------------------
	'IBM_GGP_JS1_X':('IBM_GGP_JS1_X', 'ibm_ggp_axis'),
	'IBM_GGP_JS1_Y':('IBM_GGP_JS1_Y', 'ibm_ggp_axis'),
	'IBM_GGP_JS2_X':('IBM_GGP_JS2_X', 'ibm_ggp_axis'),
	'IBM_GGP_JS2_Y':('IBM_GGP_JS2_Y', 'ibm_ggp_axis'),
	# --------------------
	'IBM_GGP_JS1_XP':('IBM_GGP_JS1_XP', 'ibm_ggp_half_axis'),
	'IBM_GGP_JS1_XN':('IBM_GGP_JS1_XN', 'ibm_ggp_half_axis'),
	'IBM_GGP_JS1_YP':('IBM_GGP_JS1_YP', 'ibm_ggp_half_axis'),
	'IBM_GGP_JS1_YN':('IBM_GGP_JS1_YN', 'ibm_ggp_half_axis'),
	'IBM_GGP_JS2_XP':('IBM_GGP_JS2_XP', 'ibm_ggp_half_axis'),
	'IBM_GGP_JS2_XN':('IBM_GGP_JS2_XN', 'ibm_ggp_half_axis'),
	'IBM_GGP_JS2_YP':('IBM_GGP_JS2_YP', 'ibm_ggp_half_axis'),
	'IBM_GGP_JS2_YN':('IBM_GGP_JS2_YN', 'ibm_ggp_half_axis'),
}

code_value_to_name_lookup = {
	0x130:{'BTN_SOUTH', 'BTN_A'},
	0x131:{'BTN_EAST', 'BTN_B'},
	0x132:{'BTN_C'},
	0x133:{'BTN_NORTH', 'BTN_X'},
	0x134:{'BTN_WEST', 'BTN_Y'},
	0x135:{'BTN_Z'},
	0x136:{'BTN_TL'},
	0x137:{'BTN_TR'},
	0x138:{'BTN_TL2'},
	0x139:{'BTN_TR2'},
	0x13a:{'BTN_SELECT'},
	0x13b:{'BTN_START'},
	0x13c:{'BTN_MODE'},
	0x13d:{'BTN_THUMBL'},
	0x13e:{'BTN_THUMBR'},
	0x00:{'ABS_X'},
	0x01:{'ABS_Y'},
	0x02:{'ABS_Z'},
	0x03:{'ABS_RX'},
	0x04:{'ABS_RY'},
	0x05:{'ABS_RZ'},
	0x06:{'ABS_THROTTLE'},
	0x07:{'ABS_RUDDER'},
	0x08:{'ABS_WHEEL'},
	0x09:{'ABS_GAS'},
	0x0a:{'ABS_BRAKE'},
	0x10:{'ABS_HAT0X'},
	0x11:{'ABS_HAT0Y'},
	0x12:{'ABS_HAT1X'},
	0x13:{'ABS_HAT1Y'},
	0x14:{'ABS_HAT2X'},
	0x15:{'ABS_HAT2Y'},
	0x16:{'ABS_HAT3X'},
	0x17:{'ABS_HAT3Y'},
	373:{'BTN_MODE'},
}

board_id_lookup = {
	'Unknown':0,
	'IBMPC':1,
	'ADB':2,
}

protocol_id_lookup = {
	'OFF':0,
	'AT_PS2_KB':1,
	'XT_KB':2,
	'ADB_KB':3,
	'PS2_MOUSE':4,
	'MICROSOFT_SERIAL_MOUSE':5,
	'ADB_MOUSE':6,
	'GAMEPORT_15PIN_GAMEPAD':7,
	'GAMEPORT_GRAVIS_GAMEPAD':8,
	'GAMEPORT_MICROSOFT_SIDEWINDER':9,
	'RAW_KEYBOARD':125,
	'RAW_MOUSE':126,
	'RAW_GAMEPAD':127,
}
