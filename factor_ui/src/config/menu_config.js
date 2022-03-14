// 动态生成菜单
import {
    AppstoreOutlined,
    HomeOutlined,
    MailOutlined,
    BarsOutlined,
    TagsOutlined,
    FileTextOutlined,
    CommentOutlined,
    FrownOutlined,
    AlertOutlined,
    AndroidOutlined,
    BankOutlined,
    PayCircleOutlined,
    MoneyCollectOutlined,
    TeamOutlined
} from '@ant-design/icons';
const menuList=[
    {
        title:'首页',
        key:'home',
        icon:HomeOutlined,
        path:'/home'
    },
    {
        title:'土地信息',
        key:'land_information',
        icon: BankOutlined,
        children:[
            {
                title:'供给数据',
                key:'supply_data',
                icon:MoneyCollectOutlined,
                path:'/land_information/supply_data'
            },
            {
                title:'成交数据',
                key:'transaction_data',
                icon:PayCircleOutlined,
                path:'/land_information/transaction_data'
            },
        ]
    },
    {
        title:'人口信息',
        key:'population_data',
        icon:TeamOutlined,
        path:'/population_data'
    },
    {
        title:'舆情信息',
        key:'public_sentiment',
        icon: AppstoreOutlined ,
        path: '/public_sentiment'
    },
    {
        title:'信息管理',
        key:'news_mgt',
        icon: MailOutlined,
        children:[
            {
                title:'申诉管理',
                key:'complaint',
                icon:FrownOutlined,
                path:'/news_mgt/complaint'
            },
            {
                title:'举报管理',
                key:'report',
                icon:AlertOutlined,
                path:'/news_mgt/report'
            },
        ]
    },
    {
        title:'App版本管理',
        key:'app',
        icon:AndroidOutlined,
        path:'/appversion_mgt'
    },
]
export default menuList
