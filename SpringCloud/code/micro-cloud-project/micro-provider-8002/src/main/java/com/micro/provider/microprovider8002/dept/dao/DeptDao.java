package com.micro.provider.microprovider8002.dept.dao;

import com.entity.Dept;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;


@Mapper
public interface DeptDao {
    List<Dept> selectlist();
}
