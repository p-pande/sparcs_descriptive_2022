# SPARCS Descriptive 2022

I copied the API url from the website and used it to extract the data. 

The average length of stays for Nassau county based on the 50,000 rows I focused on was 5.5 days. 

I had to use the low_memory parameter to false when importing allows pandas more memory to process the data and this helped fix the issue when I specified to use certain columns 

I also converted data to numeric or else it only displayed count, unique, top and freq
errors ='coerce' turned any non-numeric values to NaN

As expected, the highest admission type was "Emergency" with the frequency of 33,650 visits out of the 50,000

For charges, the average was at 359.72 with the max reaching up to 945.42.