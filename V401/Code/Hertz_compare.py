
from ultimate_plotting_v9 import *

dateinamen = ["U2_2V", "T_170", "T_175", "T_181"]

def ultimate_plot_T():
    
    colors = sns.color_palette("magma", 4)

    sample_format_dict_1 = {
        "label"      : r"T = $(165 \pm 1)C$",          
        "fmt"        : '-o', 
        "color"      : colors[0],                               
        "markersize" : 1.5, 
        "linewidth"  : 1,
        "capsize"    : 0,
        "alpha"      : 1                                   
    }
    sample_format_dict_2 = {
        "label"      : r"T = $(170 \pm 1)C$",          
        "fmt"        : '-o', 
        "color"      : colors[1],                               
        "markersize" : 1.5, 
        "linewidth"  : 1,
        "capsize"    : 0,
        "alpha"      : 1                                   
    }
    sample_format_dict_3 = {
        "label"      : r"T = $(175 \pm 1)C$",          
        "fmt"        : '-o', 
        "color"      : colors[2],                               
        "markersize" : 1.5, 
        "linewidth"  : 1,
        "capsize"    : 0,
        "alpha"      : 1                                   
    }
    sample_format_dict_4 = {
        "label"      : r"T = $(181 \pm 1)C$",          
        "fmt"        : '-o', 
        "color"      : colors[3],                               
        "markersize" : 1.5, 
        "linewidth"  : 1,
        "capsize"    : 0,
        "alpha"      : 1                                   
    }
    writtings = {
        "title"       : None,
        "x_ax_label"  : r"Beschleunigungsspannung $U_1$ [$V$]",
        "y_ax_label"  : r"Anodenspannung $U_A$ [V]"
    }
    
    general_format_dict = standard_format_dict.copy()
    zoom_params         = no_zooming.copy()
    colorbar_params     = no_colorbar.copy()
    extra_label         = no_extra_label.copy()
    
    all_data            = []
    for i in range(len(dateinamen)):
        data = np.loadtxt("../Data_Hertz/"+dateinamen[i]+".txt", skiprows=5)
        U_acc       = data[:, 2]
        U_meas      = data[:, 3 ]
        U_meas_err  = np.abs(U_meas * 0.02)
        all_data.append( [U_acc, None, U_meas, None] )

    all_sample_format_dicts = [ sample_format_dict_1, sample_format_dict_2, sample_format_dict_3, sample_format_dict_4 ]
    save_plot = True, "../Figures/Temperatures.jpg"                                     
    ultimate_plot_advanced (all_data, writtings, zoom_params, colorbar_params, extra_label, save_plot, all_sample_format_dicts, general_format_dict)

ultimate_plot_T()
ultimate_plot_T()


dateinamen = ["U2_2V", "U2_2-5V", "U2_3V", "U2_3-5V"]

def ultimate_plot_U():
    
    colors = sns.color_palette("magma", 4)

    sample_format_dict_1 = {
        "label"      : r"$U_2 = (2.0 \pm 0.1)V $",          
        "fmt"        : '-o', 
        "color"      : colors[0],                               
        "markersize" : 1.5, 
        "linewidth"  : 1,
        "capsize"    : 0,
        "alpha"      : 1                                   
    }
    sample_format_dict_2 = {
        "label"      : r"$U_2 = (2.5 \pm 0.1)V $",          
        "fmt"        : '-o', 
        "color"      : colors[1],                               
        "markersize" : 1.5, 
        "linewidth"  : 1,
        "capsize"    : 0,
        "alpha"      : 1                                   
    }
    sample_format_dict_3 = {
        "label"      : r"$U_2 = (3.0 \pm 0.1)V $",          
        "fmt"        : '-o', 
        "color"      : colors[2],                               
        "markersize" : 1.5, 
        "linewidth"  : 1,
        "capsize"    : 0,
        "alpha"      : 1                                   
    }
    sample_format_dict_4 = {
        "label"      : r"$U_2 = (3.5 \pm 0.1)V $",          
        "fmt"        : '-o', 
        "color"      : colors[3],                               
        "markersize" : 1.5, 
        "linewidth"  : 1,
        "capsize"    : 0,
        "alpha"      : 1                                   
    }
    writtings = {
        "title"       : None,
        "x_ax_label"  : r"Beschleunigungsspannung $U_1$ [$V$]",
        "y_ax_label"  : r"Anodenspannung $U_A$ [V]"
    }
    
    general_format_dict = standard_format_dict.copy()
    zoom_params         = no_zooming.copy()
    colorbar_params     = no_colorbar.copy()
    extra_label         = no_extra_label.copy()
    
    all_data            = []
    for i in range(len(dateinamen)):
        data = np.loadtxt("../Data_Hertz/"+dateinamen[i]+".txt", skiprows=5)
        U_acc       = data[:, 2]
        U_meas      = data[:, 3 ]
        U_meas_err  = np.abs(U_meas * 0.02)
        all_data.append( [U_acc, None, U_meas, None] )

    all_sample_format_dicts = [ sample_format_dict_1, sample_format_dict_2, sample_format_dict_3, sample_format_dict_4 ]
    save_plot = True, "../Figures/Bremsspannungen.jpg"                                     
    ultimate_plot_advanced (all_data, writtings, zoom_params, colorbar_params, extra_label, save_plot, all_sample_format_dicts, general_format_dict)

ultimate_plot_U()
