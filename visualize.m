%% Load Data
data = readtable('jena_covid19_scraped.csv');
data(7,:) = []; % remove early day numbers for 17th

%% Plot with normal scaling
subplot(1,1,1);
plot(data.date, data.case_number, '.-','MarkerSize', 40,'LineWidth',2);
grid on;
grid minor;
a = gca;
a.XAxis.LineWidth = 2;
a.YAxis.LineWidth = 2;
a.FontSize = 20;
set(gcf,'color','white');
title('COVID-19 cases in Jena');

diffCases = diff(data.case_number);
for iDiff = 1:length(diffCases)
    hold on;
    text(data.date(iDiff)+0.5, data.case_number(iDiff) + diffCases(iDiff) / 2 - 1.5, sprintf('+%i',diffCases(iDiff)),'FontSize',18,'HorizontalAlignment','Left');
end
hold off;
ylim([-3, 100]);
%a.XLim = [datetime('2020-03-11'), datetime('2020-03-22')]
img = getframe(gcf);
imwrite(img.cdata, 'casesJena.png')

%% Logarithmic scaling
subplot(1,1,1);
semilogy(data.date, data.case_number, '.-','MarkerSize', 40,'LineWidth',2);
grid on;
grid minor;
a = gca;
a.XAxis.LineWidth = 2;
a.YAxis.LineWidth = 2;
a.FontSize = 20;
set(gcf,'color','white');
title('COVID-19 cases in Jena');

diffCases = diff(data.case_number);
for iDiff = 1:length(diffCases)
    hold on;
    text(data.date(iDiff)+0.5, data.case_number(iDiff) + diffCases(iDiff) / 2 - 1.5, sprintf('+%i',diffCases(iDiff)),'FontSize',18);
end
hold off;

img = getframe(gcf);
imwrite(img.cdata, 'casesJenaLog.png')