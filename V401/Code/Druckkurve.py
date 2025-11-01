from ultimate_plotting_v9 import * 

    # T in Grad Celsius ---> log(p)
def druckkurve( T ):
    return 10.55 - 3333/(T+273.15) - 0.85*np.log(T+273.15)


T_array         = np.linspace(0, 300, 200)
log_p_array     = druckkurve(T_array)

def ultimate_plot():
    
    sample_format_dict_1 = {
        "label"      : None,          
        "fmt"        : '-', 
        "color"      : sns.color_palette("dark")[0],                               
        "markersize" : 4, 
        "linewidth"  : 1,
        "capsize"    : 0,
        "alpha"      : 1                                   
    }
 
    writtings = {
        "title"       : None,
        "x_ax_label"  : r"Temperatur $T$ [Grad $C$]",
        "y_ax_label"  : r"Log. Druck $\log{(\frac{p}{1 Torr})}$ [1]"
    }
    
    general_format_dict = standard_format_dict.copy()
    zoom_params         = no_zooming.copy()
    colorbar_params     = no_colorbar.copy()
    extra_label         = no_extra_label.copy()
    
    data_set_1  = T_array, None, log_p_array, None 
    
    all_data                = [ data_set_1 ]                               
    all_sample_format_dicts = [ sample_format_dict_1 ]
    save_plot = True, "../Figures/Druckkurve.jpg"                                     
    ultimate_plot_advanced (all_data, writtings, zoom_params, colorbar_params, extra_label, save_plot, all_sample_format_dicts, general_format_dict)

ultimate_plot()
ultimate_plot()