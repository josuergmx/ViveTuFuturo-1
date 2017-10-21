package com.project.vive.repository;

import java.io.Serializable;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.project.vive.entity.Direccion;

@Repository("direccionRepository")
public interface DireccionRepository extends JpaRepository<Direccion, Serializable> {
	public abstract Direccion findById(Integer id);
}
