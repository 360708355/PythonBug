# coding=utf-8
import codecs
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]

    def collect_data(self,data):
        if data is not None:
            self.datas.append(data)

    def output_html(self):
        print(len(self.datas))
        fout=codecs.open('output.html','w','utf-8')
        fout.write('<html>')
        fout.write('<body>')

        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')

            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
#             print('%s' % data['summary'].encode('utf-8'))
            try:
                fout.write('<td>%s</td>' % data['summary'])
            except:
                print('write Error')
            fout.write('</tr>')

        fout.write('</table>')

        fout.write('</body>')
        fout.write('</html>')
        fout.close()
    
    
    
    



