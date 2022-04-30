// 动态生成菜单
import {
    AppstoreOutlined,
    HomeOutlined,
    BarChartOutlined,
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
        title:'城市信息',
        key:'city_information',
        icon:TeamOutlined,
        path:'/city_information'
    },
    {
        title:'舆情信息',
        key:'public_sentiment',
        icon: AppstoreOutlined ,
        path: '/public_sentiment'
    },
    {
        title:'楼市分析',
        key:'/detail_data',
        icon: BarChartOutlined,
        path:'/detail_data'
    },
]
export default menuList
