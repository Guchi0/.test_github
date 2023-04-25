% format:
% https://www.biosemi.com/faq/file_format.htm
%
% sample script: 
% https://jp.mathworks.com/matlabcentral/fileexchange/13070-eeg-bdf-reader
%
% cf: edf-browser
% https://www.teuniz.net/edfbrowser/
% 
% Memo copoed from manual:
% BDF+ format, the 24 bit version of a European Data Format (EDF+) file
%
% Note that EDF supports 16 bit data values only. Thus both the
% resolution and range are compromised when fitting Avatar's 24-bit data values into an EDF file. BDF+ is a standard very
% similar to EDF except that it supports 24-bit data values. BDF+ files can be created from an Avatar EEG recorder native
% binary file by following the instructions previously outlined for creating an EDF file, but substituting the program
% rec2bdf.py for rec2edf.py. Output files will have the extension .bdf.