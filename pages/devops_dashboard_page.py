# @author liruohao
# @create 2017-11-2


class DevopsDashboardPage:
    # 通用
    url = 'http://172.17.123.177:8080/#/dashboard/home'
    navigation = 'div.ant-menu-submenu-title'
    header = 'section.content-header'
    tableBody = 'tbody.ant-table-tbody'
    tableTrTime0 = '//tbody[@class="ant-table-tbody"]/tr[1]/td[4]'
    tableTrTime1 = '//tbody[@class="ant-table-tbody"]/tr[2]/td[4]'
    tableTrName0 = '//tbody[@class="ant-table-tbody"]/tr[1]/td[1]'
    tableTrName1 = '//tbody[@class="ant-table-tbody"]/tr[2]/td[1]'
    btnModalAccept = '//button[contains(.,"确")]'
    inputKeywordSearch = 'input#searchKeyword'
    btnSearch = '//button[contains(.,"搜")]'
    iconNoData = 'i.anticon-frown-o'
    inputModalAutoComplete = '//div[@class="ant-modal"]/descendant::input[@class="ant-input ant-select-search__field"]'
    inputAppAutoComplete = '//div[@id="app"]/descendant::input[@class="ant-input ant-select-search__field"]'
    selectModal = '//div[@class="ant-modal"]/descendant::div[@role="combobox"]'
    selectApp = '//div[@id="app"]/descendant::div[@role="combobox"]'

    # 服务配置
    ## 服务接入配置
    menuServiceInsertManage = "//a[contains(.,'服务接入配置')]"
    menuServiceMange = "//span[contains(.,'服务配置')]"
    btnAddService = '//button[contains(.,"添加服务")]'
    modalInputServiceInsertServerName = 'input#name'
    modalRadioServiceInsertNeedBalance = 'span.ant-radio'
    modalTextareaServiceInsertServerIP = 'textarea#ips'
    modalTextareaServiceInsertDescription = 'textarea#description'
    tableTrIP = '//tbody[@class="ant-table-tbody"]/tr[1]/td[2]'
    detailIP = 'span.detail-value'

    ### 服务文档

    ## api网关设置
    menuAPIManage = "//a[contains(.,'API配置')]"
    btnAddAPI = '//button[contains(.,"添加API配置")]'
    modalInputApiName = 'input#name'
    modalInputApiGatePath = 'input#gatePath'
    modalInputApiSubPath = 'input#subPath'
    modalInputApiPath = 'input#apiPath'
    modalDivSelect = '//div[@role="combobox" and contains(.,"无")]'
    modalDivOption = '//div[contains(.,"HMAC")]'
    tableTrPath = '//tbody[@class="ant-table-tbody"]/tr[1]/td[2]'
    detailPath = 'span.detail-value'
    tableTrApiTime0 = '//tbody[@class="ant-table-tbody"]/tr[1]/td[7]'
    tableTrApiTime1 = '//tbody[@class="ant-table-tbody"]/tr[2]/td[7]'

    # 服务使用
    ## 服务授权管理
    menuServiceAuth = "//a[contains(.,'服务授权管理')]"
    btnAddAuthProject = '//button[contains(.,"添加授权项目")]'
    liCanceled = "//li[contains(.,'已取消')]"
    tableTrProjectName = '//tbody[@class="ant-table-tbody"]/tr/td[1]'
    tableTrAuthTime0 = '//tbody[@class="ant-table-tbody"]/tr[1]/td[5]'
    tableTrAuthTime1 = '//tbody[@class="ant-table-tbody"]/tr[2]/td[5]'
    divAuthFilterText = 'div.ant-select-selection-selected-value'

    ## 业务方管理
    menuConsumerManage = '//a[contains(.,"业务方管理")]'
    btnAddConsumer = '//button[contains(.,"创建业务方")]'
    modalInputConsumerName = 'input#bizName'
    modalInputConsumerManager = 'input#manager'
    modalInputConsumerPhone = 'input#phone'
    modalInputConsumerEmail = 'input#email'

    ## 项目管理
    menuProjectManage = '//a[contains(.,"项目管理")]'
    btnAddProject = '//button[contains(.,"创建项目")]'
    tableTrProjectManageTime0 = '//tbody[@class="ant-table-tbody"]/tr[1]/td[5]'
    tableTrProjectManageTime1 = '//tbody[@class="ant-table-tbody"]/tr[2]/td[5]'
    modalInputProjectName = 'input#name'

    ## 应用管理
    menuAppManage = '//a[contains(.,"应用管理")]'
    btnAddApp = '//button[contains(.,"创建应用")]'
    modalInputAppName = 'input#name'
    tableTrAppManageTime0 = '//tbody[@class="ant-table-tbody"]/tr[1]/td[7]'
    tableTrAppManageTime1 = '//tbody[@class="ant-table-tbody"]/tr[2]/td[7]'
    tableTrAppClientId = '//tbody[@class="ant-table-tbody"]/tr[1]/td[2]'

    ## 联系人管理
    menuContactManage = '//a[contains(.,"联系人管理")]'
    btnAddContact = '//button[contains(.,"创建联系人")]'
    modalInputContactName = 'input#name'
    modalInputContactPhone = 'input#phone'
    modalInputContactEmail = 'input#email'

    # 其他
    ## 公告管理
    menuNoticeManage = '//a[contains(.,"公告管理")]'
    btnAddNotice = '//button[contains(.,"创建公告")]'
    modalInputNoticeTitle = 'input#title'
    modalTextareaNoticeContent = 'textarea#content'
    tableTrNoticeTime0 = '//tbody[@class="ant-table-tbody"]/tr[1]/td[3]'
    tableTrNoticeTime1 = '//tbody[@class="ant-table-tbody"]/tr[2]/td[3]'
    tableTrNoticeName0 = '//tbody[@class="ant-table-tbody"]/tr[1]/td[2]'
    tableTrNoticeName1 = '//tbody[@class="ant-table-tbody"]/tr[2]/td[2]'

    ## 业务方账号
    menuAccountManage = '//a[contains(.,"业务方账号")]'
    btnAddAccount = '//button[contains(.,"创建业务方账号")]'
    modalInputAccountName = 'input#accountName'
    modalButtonAccountGenerate = '//button[contains(.,"生")]'
    tableTrAccountTime0 = '//tbody[@class="ant-table-tbody"]/tr[1]/td[5]'
    tableTrAccountTime1 = '//tbody[@class="ant-table-tbody"]/tr[2]/td[5]'





















