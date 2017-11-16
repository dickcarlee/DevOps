# @author liruohao
# @create 2017-11-1


class DevopsPlatformPage:
    urlHomePage = 'http://172.17.123.177:8080//#/dashboard/home'
    urlSysManage = 'http://172.17.123.177:8080//#/platform/system-manage'
    btnPlatform = "//a[contains(.,'平台管理')]"
    TableBody = 'tbody.ant-table-tbody'
    iconNoData = 'i.action-frown-o'
    btnModelAccept = '//button[contains(.,"确")]'
    btnSearch = '//button[contains(.,"搜")]'
    inputKeywordSearch = 'input#searchKeyword'


    # 系统配置
    menuSysConfig = "//a[contains(.,'系统配置')]"
    tableTdSysConfigTime0 = '//tbody[@class="ant-table-tbody"]/tr[1]/td[6]'
    tableTdSysConfigTime1 = '//tbody[@class="ant-table-tbody"]/tr[2]/td[6]'
    btnNewSys = '//button[contains(.,"添加系统")]'
    inputName = 'input#name'
    inputAccountName = 'input#accountName'
    textareaAccessIps = 'textarea#accessIps'
    textareaDescription = 'textarea#description'
    btnFreeze = 'i.anticon-lock'

    # 日志信息
    menuLog = "//a[contains(.,'日志信息')]"
    tableTdLogTime0 = '//tbody[@class="ant-table-tbody"]/tr[1]/td[4]'
    tableTdLogTime1 = '//tbody[@class="ant-table-tbody"]/tr[2]/td[4]'
    tableTrLogName0 = '//tbody[@class="ant-table-tbody"]/tr[1]/td[1]'
    tableTrLogName1 = '//tbody[@class="ant-table-tbody"]/tr[2]/td[1]'




