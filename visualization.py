import matplotlib.pyplot as plt
import numpy as np

def create_radar_chart(analysis_data):
    categories = ['Karakteristik', 'Pendidikan', 'Pengalaman', 'Potensi Gaji', 'Prospek Kerja']
    values = [
        analysis_data['subscores']['trait_score'],
        analysis_data['subscores']['education_score'],
        analysis_data['subscores']['experience_score'],
        80,  
        70   
    ]
    
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    
    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(projection='polar'))
    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    plt.title('Analisis Kesusaian Karir')
    return fig