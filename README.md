Subsequent Contents: (maximum 2-3 pages)

1.	Abstract
2.	Problem Definition.
3.	Motivations/ Objectives: 
4.	Facilities required for proposed work: (Software/Hardware required for the development of the project.).
5.	Bibliography/References: (Here specify the description of the study material referred for the development of the project.)



Abstract

Asthma, a chronic respiratory condition characterized by inflammation and hypersensitivity of the airways, continues to pose a significant health concern, especially among children. Environmental factors play a crucial role in triggering asthma attacks, with air pollution, temperature fluctuations, and humidity levels being prominent culprits. These triggers can exacerbate respiratory symptoms, leading to wheezing, shortness of breath, and coughing, and in severe cases, necessitate emergency medical intervention. 

Recognizing the pressing need for proactive asthma management, particularly in regions like Qatar where environmental conditions may exacerbate symptoms, our study proposes a novel system designed to prevent asthma attacks by providing real-time air quality information to parents. Our innovative solution comprises two interconnected subsystems: an Air-Quality Sensing Subsystem (AQSS) and a mobile application. 

The AQSS is equipped with an array of sensors strategically positioned to gather data on critical environmental factors known to exacerbate asthma attacks in our region, including temperature, humidity, dust particles, and Carbon Monoxide (CO) levels. This subsystem continuously collects and processes environmental data in real-time, analyzing the safety of the air quality for asthmatic children. Through advanced algorithms and sensor fusion techniques, the AQSS evaluates the collected data to assess the risk of asthma triggers in the surrounding environment. 

The processed data, along with real-time alerts and notifications, is seamlessly transmitted wirelessly to a dedicated smartphone application via Bluetooth technology. The mobile application serves as a user-friendly interface, presenting parents with comprehensive air quality metrics and personalized recommendations tailored to their child's specific asthma needs. Through intuitive visualizations and easy-to-understand indicators, parents are promptly informed about the suitability of the external air quality for their asthmatic children.

 Empowered with timely and actionable information, parents can proactively implement preventive measures to safeguard their children from potential asthma triggers. Whether adjusting indoor ventilation, initiating air purification measures, or avoiding outdoor activities during periods of poor air quality, our system enables parents to make informed decisions to protect their child's respiratory health. 

By focusing on prevention rather than reactive management, our system aims to stabilize the health condition of asthmatic children, thereby reducing the frequency and severity of asthma attacks. Through early intervention and proactive asthma management, we anticipate a decrease in the reliance on costly hospitalization procedures, alleviating the burden on healthcare systems and improving the overall quality of life for asthmatic children and their families.


Problem Definition.
Problem Definition:

Asthma is a chronic respiratory condition where airways become inflamed and hypersensitive to triggers, leading to symptoms like wheezing, shortness of breath, and coughing. Indoor air pollution is a major risk factor for asthma attacks, as exposure to various triggers can worsen symptoms. Traditional asthma management focuses on medication and avoiding known allergens, but these strategies lack real-time data on specific triggers present in a patient's environment.

Problem Statement

Current asthma management strategies have limitations:

Limited Awareness of Triggers: Patients often struggle to identify specific triggers within their homes, making it difficult to take targeted preventative measures.
Reliance on General Awareness: Existing solutions rely on patients knowing all potential triggers, which may be incomplete or inaccurate.
Lack of Real-time Data: Traditional methods don't provide real-time information on fluctuations in air quality, hindering proactive adjustments to the environment.
Desired Outcomes

This project seeks to develop a comprehensive indoor air quality monitoring system specifically designed for asthma patients. This system will address the limitations mentioned above by:
Accurate Trigger Measurement: Utilizing reliable sensor technology to monitor key pollutants and potential asthma triggers like VOCs, PM2.5, and mold spores.
Actionable Data Presentation: Translating air quality data into clear, user-friendly information for patients. This includes:
Real-time readings on trigger levels.
Easy-to-understand indicators of air quality risk for asthma.
Personalized recommendations based on individual sensitivity and asthma management plans.
Patient Empowerment: Enabling patients to take control of their environment through proactive measures based on real-time data. Examples include:
Alerts for exceeding trigger thresholds.
Recommendations for ventilation, air purification, or allergen removal strategies.
Potential integration with smart home devices to automate air quality control.
Additionally, the system should ideally support medical integration by:

Connecting with existing asthma management plans and healthcare providers.
Facilitating data sharing with doctors for informed treatment decisions.
Enabling the identification of triggers and development of personalized management strategies.
Challenges

Sensor Accuracy and Affordability: Balancing the need for accurate detection of a wide range of triggers with affordability for patients.
Actionable Insights: Developing a system that interprets data and provides clear, tailored recommendations for different situations.
Data Privacy and Security: Ensuring robust security measures to protect sensitive health information collected by the system.
Accessibility and Usability: Designing a user-friendly system that caters to patients with varying technical expertise and economic backgrounds.
Integration with Healthcare: Overcoming potential hurdles in integrating the system with existing healthcare infrastructure and workflows.
Overall Impact
This project aims to bridge the gap between traditional asthma management and real-time air quality data. By empowering patients with actionable information and facilitating communication with healthcare professionals, this system has the potential to significantly improve asthma control and quality of life for patients.


Motivations/ Objectives:
Monitoring indoor air quality is critical for patients with asthma, as exposure to indoor pollutants can exacerbate respiratory symptoms and lead to distressing asthma attacks. Despite the significant impact of indoor air pollution on asthma management, existing monitoring solutions often fail to meet the specific needs of asthma patients. To address this gap, our research endeavors to develop an innovative indoor air quality monitoring system tailored explicitly for individuals with asthma.

Our proposed system harnesses the latest advancements in sensor technology and analytics to provide asthma patients with access to real-time information about the quality of air in their indoor environments. By deploying cutting-edge sensors strategically throughout the indoor space, our system continuously monitors key pollutants and triggers known to worsen asthma symptoms, including volatile organic compounds (VOCs), particulate matter (PM2.5), and mold spores. This real-time monitoring capability empowers patients to make informed decisions about their surroundings, enabling them to take proactive measures to mitigate potential asthma triggers and reduce the risk of exacerbations.

One of the distinguishing features of our system is its ability to offer personalized recommendations for interventions based on individual asthma triggers. Through sophisticated analytics and machine learning algorithms, our system analyzes the collected data to identify patterns and correlations between indoor air quality parameters and asthma symptoms. By pinpointing specific triggers unique to each patient, our system provides tailored recommendations for interventions, such as adjusting ventilation, using air purifiers, or implementing allergen avoidance strategies. These personalized recommendations not only help asthma patients better manage their condition but also contribute to improving their overall quality of life.

Furthermore, our technology facilitates seamless communication and collaboration between patients and medical professionals, fostering proactive monitoring and timely interventions. By securely sharing anonymized data with healthcare providers, our system enables clinicians to gain insights into patients' asthma triggers and disease patterns, facilitating more informed treatment decisions and personalized care plans. This integration between technology and healthcare not only enhances patient outcomes but also advances asthma research and informs public health policies aimed at reducing the burden of asthma on society.

In summary, our innovative indoor air quality monitoring system for asthma patients represents a significant advancement in asthma management. By providing real-time information, personalized recommendations, and facilitating collaboration between patients and healthcare providers, our system has the potential to improve asthma control, enhance patient well-being, and ultimately reduce the socioeconomic impact of asthma on individuals and communities.


Facilities required for proposed work:
In the initial phases of our project, we employed the Mbed development board for prototyping purposes. This versatile platform provided us with the flexibility and functionality needed to integrate various sensor modules and develop the necessary software for our indoor air quality monitoring system.

Each sensor module selected for our system was carefully evaluated and studied to ensure its compatibility and effectiveness in measuring key environmental factors known to impact asthma triggers. Here's a breakdown of the sensor modules utilized in our prototype:

1.	Dust Sensor (PMS5003): The PMS5003 dust sensor module was chosen for its ability to detect small particles suspended in the air, which can pose a significant risk to the respiratory health of asthmatic children. By accurately measuring particulate matter concentrations, this sensor enables us to monitor air quality and identify potential triggers for asthma exacerbations.

2.	Humidity and Temperature Sensor (Grove SEN51035P): The Grove humidity sensor SEN51035P was integrated into our Air-Quality Sensing Subsystem to provide real-time measurements of both humidity and temperature. This dual functionality is crucial for assessing indoor air quality, as humidity levels can influence the proliferation of allergens and mold, while temperature variations can affect respiratory comfort and exacerbate asthma symptoms.

3.	Carbon Monoxide Sensor (MQ-7): The MQ-7 carbon monoxide (CO) sensor module was selected to monitor air pollution levels and detect the presence of this hazardous gas, which can pose serious health risks, particularly for individuals with respiratory conditions like asthma. The MQ-7 sensor is interfaced directly with the Mbed Microcontroller, enabling seamless integration and communication with the main system.

Interfacing each sensor module with the Mbed MCU involved connecting the respective digital or analog output pins of the sensors to GPIO ports or analog input ports of the Mbed Microcontroller. This hardware integration allowed us to acquire raw data from the sensors and process it in real-time to assess indoor air quality and identify potential asthma triggers.

On the software side, we developed custom programs for the Mbed MCU to initialize, calibrate (if necessary), and acquire raw data from the sensor modules. Advanced algorithms were implemented to manipulate and analyze the sensor data, enabling the system to make informed decisions regarding air quality and trigger identification. Additionally, we incorporated functionality to wirelessly transmit processed data and alert messages using Bluetooth Low Energy (BLE) technology to a host computer for testing and further analysis.

By integrating cutting-edge sensor technology with the Mbed development platform and developing robust software algorithms, our prototype indoor air quality monitoring system demonstrates the feasibility and effectiveness of our approach in providing real-time air quality information to aid in asthma management and prevention.


Bibliography/References:


1.	Al-Neaimi, Y., Gomes, J., & Al-Maskari, F. (2016). Asthma and indoor environmental factors in the United Arab Emirates. International Journal of Environmental Research and Public Health, 13(1), 101.
2.	World Health Organization. (2020). Asthma. 
3.	Gorman, D. (2018). Indoor Air Quality and Health. International Journal of Environmental Research and Public Health, 15(7), 1471. 
4.	Amjad, A. (2019). Asthma in Qatar: An Overview. Qatar Medical Journal, 2019(2), 1-11. 
5.	Ghazal, S., & Al Khulaifi, M. M. (2019). Prevalence and associated factors of asthma among adults in Qatar: A community-based survey. Medical Principles and Practice, 28(4), 318-326. 
6.	Sankaranarayanan, K., & Hariharan, S. (2018). Indoor Air Pollution: A Comprehensive Review. Journal of Environmental and Public Health, 2018, 17. 
7.	Wang, C., Liu, Q., & Piao, S. (2019). The impact of indoor air quality on respiratory health in China. Environmental Research, 174, 210-215. 
8.	Delfino, R. J., & Wu, J. (2018). Asthma morbidity and ambient air pollution: Effect modification by residential traffic-related air pollution. Epidemiology, 29(1), 66-74.
9.	U.S. Environmental Protection Agency. (2020). Indoor Air Quality (IAQ). 
10.	Taylor, S., & King, R. (2018). Evaluating the AQHI in Canada: Asthma as a Public Health Surveillance Indicator. International Journal of Environmental Research and Public Health, 15(12), 2663.

