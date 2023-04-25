function test_bdf_satonao2
%
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
%


% ============================================ TEST 2b
clf
cstr = input('enter str? ','s');  % ex. Avatar_04137_2022-08-01_18-20-39
fnm = strcat(cstr,'.bdf');
fnm

fclose all
fid = fopen( fnm );
numChan = 30; % empirical value 
fseek(fid,256*(17+1),'bof'); % % should be corrected, too long 
dat = [];
while 1 % ~feof( fid )

    pos1 = ftell( fid ); 
    aux = fread(fid,[ 1, numChan],'bit24')';

    if length( aux ) == numChan
        dat=[dat, aux];
    else
        fseek( fid, pos1,'bof' );
    end
    if mod( size( dat, 2), 500 ) == 0
        plot( dat( numChan - 10 + 1 , : ) );
        drawnow
    end
end
% fclose(fid);
dat1 = dat( numChan - 10 + 1 , : );

return 


% ============================================ TEST 2a 
cstr = 'Avatar_04137_2022-08-01_17-40-14';

% ---------------------------- test read csv 
fnm = strcat(cstr,'.csv');
fnm
fid = fopen( fnm, 'r');
cl1 = fgetl( fid ) ; % header 
i=1;
while ~feof( fid )
    cl1 = fgetl( fid ) ; 
    C = strsplit( cl1 ); % length(C) = 13 
    x(i) = str2num( C{13-8+1}); % ch1
    i=i+1;
end
fclose( fid )
plot( x ) 

% -----------------------------test read bdf 
fnm = strcat(cstr,'.bdf');
fnm
fid = fopen( fnm );
numChan = 30; % empirical value 
fseek(fid,256*(17+1),'bof'); % % should be corrected, too long 
dat = [];
while ~feof( fid ) % for i=1:10
    aux = fread(fid,[ 1, numChan],'bit24')';
 
    if length( aux ) == numChan
        dat=[dat, aux];
    end
end
fclose(fid);
dat1 = dat( numChan - 10 + 1 , : );

hold on ; 
plot( dat1 ) 
hold off 

return 

