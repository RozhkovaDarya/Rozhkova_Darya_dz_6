import re

def parse_log_line(log_line: str):
    ip_address, log_line = log_line.split(' - - ')
    date, log_line = log_line.split('] ')

    date = date.lstrip('[')

    request, other_info = log_line.rsplit(' "-" ')
    
    other_info = other_info.strip('"')

    request = request.replace('"', '').split(' ')

    return ip_address, request


lines = ['93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"',
         '93.180.71.3 - - [17/May/2015:08:05:23 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"',
         '80.91.33.133 - - [17/May/2015:08:05:24 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"']
parsed_lines = [parse_log_line(line) for line in lines]
print(parsed_lines)

print('\n')

def reader(filename):
    regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    with open(filename) as f:
      log = f.read()
      ips_list = re.findall(regexp, log)
    print(ips_list)
    return ips_list

 
if __name__ == '__main__':
  reader('nginx_logs.txt')