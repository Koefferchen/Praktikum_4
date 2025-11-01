
from ultimate_plotting_v9 import *

dateiname = "T_170"

data = np.loadtxt("../Data_Hertz/"+dateiname+".txt", skiprows=5)

U_acc       = data[:, 2]
U_meas      = data[:, 3 ]
U_meas_err  = np.abs(U_meas * 0.02)

def Gauß_fit(x, mu, sigma, amplitude):
    return amplitude * np.exp( -1/2 * (x-mu)**2 /sigma**2 )

# def Multi_Gauß_fit(x, mu1, sigma1, mu2, sigma2, mu3, sigma3, mu4, sigma4, mu5, sigma5, mu6, sigma6, alpha, beta):
#     return alpha**2 *( np.exp(beta*x) -1 ) * ( Gauß_fit(x, mu1, sigma1) + Gauß_fit(x, mu2, sigma2) + Gauß_fit(x, mu3, sigma3) + Gauß_fit(x, mu4, sigma4) + Gauß_fit(x, mu5, sigma5) + Gauß_fit(x, mu6, sigma6) )


#guess = np.concatenate((guess1, guess2, guess3, guess4, guess5, guess6))
#print(guess)



guess0 = (11.5, 2.0, 0.1)
guess1 = (11.5+5, 2.0, 0.4)
guess2 = (11.5+10, 2.0, 1.5)
guess3 = (11.5+15, 2.0, 4.5)
guess4 = (11.5+20, 2.0, 6.5)
guess5 = (11.5+25, 2.0, 9.5 )
guesses = np.array([guess0, guess1, guess2, guess3, guess4, guess5])

mask_peak0 = (11 < U_acc) & (U_acc < 12)
mask_peak1 = (15.5 < U_acc) & (U_acc < 17.5)
mask_peak2 = (20 < U_acc) & (U_acc < 22)
mask_peak3 = (25 < U_acc) & (U_acc < 27)
mask_peak4 = (30 < U_acc) & (U_acc < 32)
mask_peak5 = (35 < U_acc) & (U_acc < 37)
masks      = np.array([mask_peak0, mask_peak1, mask_peak2, mask_peak3, mask_peak4, mask_peak5])


peak_number         = 6
fitrange            = [0, 37.5]
fitdensity          = 200
param_matrix        = np.zeros((6, 3))
param_err_matrix    = np.zeros((6, 3))
y_fit_total         = np.zeros(fitdensity)

for peak_index in range(peak_number):
    x_fit_total, y_fit, param_matrix[peak_index], param_err_matrix[peak_index], chi2 = fit(U_acc[masks[peak_index]], U_meas[masks[peak_index]], Gauß_fit, guesses[peak_index],  fit_density=fitdensity, y_error=U_meas_err[masks[peak_index]],fit_range=fitrange)
    y_fit_total = y_fit_total + y_fit


param_matrix        = param_matrix.T
param_err_matrix    = param_err_matrix.T

mu_array            = param_matrix[0]
sigma_array         = np.abs(param_matrix[1])
amplitude_array     = param_matrix[2]

mu_err_array            = param_err_matrix[0]
sigma_err_array         = param_err_matrix[1]
amplitude_err_array     = param_err_matrix[2]


def find_deltas(mu_array, mu_err_arry):
    delta_range     = len(mu_array) - 1
    delta_array     = np.zeros(len(mu_array))
    delta_err_array = np.zeros(len(mu_array))
    
        # calc deltas and their uncertainty
    for j in range(len(mu_array)-1):
        delta_array[j] = mu_array[j+1] - mu_array[j]
        delta_err_array[j] = np.sqrt( (mu_err_array[j])**2 + (mu_err_array[j+1])**2 )

        # last entry = average of all deltas
    delta_array[len(mu_array)-1], delta_err_array[len(mu_array)-1] = stichproben_varianz( delta_array[0:len(mu_array)-1] )

    return delta_array, delta_err_array

delta_array, delta_err_array = find_deltas( mu_array, mu_err_array)

write_data      = np.array([mu_array, sigma_array, amplitude_array, delta_array])
write_data_err  = np.array([mu_err_array, sigma_err_array, amplitude_err_array, delta_err_array])

array_to_latex("../Data_Hertz/Params_" + dateiname + ".txt", write_data, write_data_err)






def ultimate_plot():
    
    sample_format_dict_1 = {
        "label"      : r"Messdaten",          
        "fmt"        : '.', 
        "color"      : "black",                               
        "markersize" : 2, 
        "linewidth"  : 1,
        "capsize"    : 0,
        "alpha"      : 1                                   
    }
    sample_format_dict_2 = {
        "label"      : f"Fit",          
        "fmt"        : '-', 
        "color"      : sns.color_palette("dark")[9],                               
        "markersize" : 2, 
        "linewidth"  : 2,
        "capsize"    : 0,
        "alpha"      : 0.6                                   
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
    
    data_set_1  = U_acc, None, U_meas, U_meas_err  
    data_set_2  = x_fit_total, None, y_fit_total, None
    all_data                = [ data_set_1, data_set_2 ]                            
    all_sample_format_dicts = [ sample_format_dict_1, sample_format_dict_2 ]
    save_plot = True, "../Figures/"+dateiname+".jpg"                                     
    ultimate_plot_advanced (all_data, writtings, zoom_params, colorbar_params, extra_label, save_plot, all_sample_format_dicts, general_format_dict)

ultimate_plot()
ultimate_plot()
