import React, {Component} from 'react';
import { Card, message, Table, Select } from 'antd';
import { DualAxes } from '@ant-design/plots';

import {reqSupplyData} from "../../../api";
import {SUCCESS_CODE} from "../../../config";

const { Option } = Select;

//表格配置
const columns = [
    {
        title: '月份',
        dataIndex: 'time',
        key: 'time',
    },
    {
        title: '供应宗数(块)',
        dataIndex: 'supply_num',
        key: 'supply_num',
        render: value => {
            if(value===0)
                return "暂无数据"
            else
                return value
        },
    },
    {
        title: '供应面积(㎡)',
        dataIndex: 'supply_area',
        key: 'supply_area',
        render: value => {
            if(value===0)
                return "暂无数据"
            else
                return value
        },
    },
    {
        title: '供应均价(元/㎡) ',
        key: 'supply_price',
        dataIndex: 'supply_price',
        render: value => {
            if(value===0)
                return "暂无数据"
            else
                return value
        },
    },
    {
        title: '楼面价(元/㎡) ',
        key: 'floor_price',
        dataIndex: 'floor_price',
        render: value => {
            if(value===0)
                return "暂无数据"
            else
                return value
        },
    },
];

class SupplyData extends Component {

    state = {
        data:[],
        chartsData:[]
    }

    //获取数据
    getDataList = (len)=>{
        reqSupplyData(len).then((res)=>{
            const {data,code,msg}= res.data
            if(code===SUCCESS_CODE){
                let chartsData=[]
                data.forEach((item)=>{
                    chartsData.push({
                        time:item.time,
                        area:item.supply_area,
                        price:item.supply_price
                    })
                })
                chartsData=chartsData.reverse()
                this.setState({
                    data,
                    chartsData
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
        const {data,chartsData} = this.state

        // 数据图配置项
        const config = {
            data: [chartsData, chartsData],
            xField: 'time',
            yField: ['area', 'price'],
            meta: {
                area: {
                    alias: '供应面积(万㎡) ',
                    formatter: (v) => {
                        return Number((v / 10000).toFixed(2));
                    },
                },
                price: {
                    alias: '供应均价(元/㎡)',
                    formatter: (v) => {
                        return v;
                    },
                },
            },
            geometryOptions: [
                {
                    geometry: 'column',
                    color: '#5B8FF9',
                    label: {
                        position: 'middle',
                    },
                },
                {
                    geometry: 'line',
                    color: '#29cae4',
                    point: {
                        size: 5,
                        shape: 'diamond',
                        style: {
                            fill: 'white',
                            stroke: '#29cae4',
                            lineWidth: 2,
                        },
                    },
                },
            ],
            xAxis: {
                label: {
                    autoRotate: true,
                    autoHide: false,
                    autoEllipsis: false,
                },
            },
            yAxis: {
                area: {
                    label: {
                        formatter: (v) => {
                            return `${v}`;
                        },
                    },
                },
                price: {
                    label: {
                        formatter: (v) => {
                            return `${v}`;
                        },
                    },

                },
            },
            legend: {
                itemName: {
                    formatter: (text, item) => {
                        return item.value === 'area' ? '供应面积(万㎡)' : '供应均价(元/㎡)';
                    },
                },
            },
        };

        return (
            <Card
                className={"data-card"}
                title={"供给数据"}
                extra={
                    <Select className="data-card-select" defaultValue="6" onChange={this.getDataList}>
                        <Option value="6">最近半年</Option>
                        <Option value="12">最近一年</Option>
                        <Option value="24">最近两年</Option>
                    </Select>
                }
                bodyStyle={{backgroundColor:'whitesmoke',padding:0,borderTop:'solid whitesmoke'}}
            >
                <div className={"data-charts"}>
                    <DualAxes {...config} />
                </div>
                <div className={"data-table"}>
                    <Table columns={columns} dataSource={data} pagination={false}/>
                </div>
            </Card>
        );
    }
}

export default SupplyData;
