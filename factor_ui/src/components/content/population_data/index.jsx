import React, {Component} from 'react';
import {Card, message, Select, Table} from "antd";
import {reqPopulationData} from "../../../api";
import {SUCCESS_CODE} from "../../../config";

const { Option } = Select;


//表格配置
const columns = [
    {
        title: '年份',
        dataIndex: 'year',
        key: 'year',
    },
    {
        title: '年末总人口(万人)',
        dataIndex: 'population_num',
        key: 'population_num',
        render: value => {
            if(value===0)
                return "暂无数据"
            else
                return value
        },
    },
    {
        title: '普通本专科学生(万人)',
        key: 'student_num',
        dataIndex: 'student_num',
        render: value => {
            if(value===0)
                return "暂无数据"
            else
                return value
        },
    },
    {
        title: '在岗职工平均工资(元)',
        dataIndex: 'average_wage',
        key: 'average_wage',
        render: value => {
            if(value===0)
                return "暂无数据"
            else
                return value
        },
    },
    {
        title: '城乡居民储蓄年末余额(亿元) ',
        key: 'savings_balance',
        dataIndex: 'savings_balance',
        render: value => {
            if(value===0)
                return "暂无数据"
            else
                return value
        },
    },
];

class PopulationData extends Component {

    state = {
        data:[],
        chartsData:[]
    }

    //获取数据
    getDataList = (len)=>{
        reqPopulationData(len).then((res)=>{
            const {data,code,msg}= res.data
            console.log(res.data)
            if(code===SUCCESS_CODE){
                // let chartsData=[]
                // data.forEach((item)=>{
                //     chartsData.push({
                //         time:item.time,
                //         area:item.supply_area,
                //         price:item.supply_price
                //     })
                // })
                // chartsData=chartsData.reverse()
                this.setState({
                    data,
                    //chartsData
                })
            }
            else{
                message.error(msg,1)
            }
        }).catch((err)=>{
            console.log(err)
        })
    }

    componentDidMount() {
        this.getDataList(6)
    }

    render() {
        const {data} = this.state
        return (
            <Card
                className={"data-card"}
                title={"人口数据"}
                extra={
                    <Select className="data-card-select" defaultValue="6" onChange={this.getDataList}>
                        <Option value="6">最近半年</Option>
                        <Option value="12">最近一年</Option>
                        <Option value="24">最近两年</Option>
                    </Select>
                }
                bodyStyle={{height:'100%',backgroundColor:'whitesmoke',padding:0,borderTop:'solid whitesmoke'}}
            >
                <div className={"data-charts"}>

                </div>
                <div className={"data-table"}>
                    <Table columns={columns} dataSource={data} pagination={false}/>
                </div>
            </Card>
        );
    }
}

export default PopulationData;
