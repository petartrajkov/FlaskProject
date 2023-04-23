class OSVersion(db.Model):
    __tablename__ = "os_version"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    # instances = db.relationship("ComputeInstance", backref="os_version", lazy=True)


class ComputeInstance(db.Model):
    __tablename__ = "compute_instance"
    id = db.Column(db.Integer, primary_key=True)
    os_version_id = db.Column(
        db.Integer, db.ForeignKey("os_version.id"), nullable=False
    )
    ip_address = db.Column(db.String(50), nullable=False)
    hostname = db.Column(db.String(50))
    created_at = db.Column(db.DateTime)
    os_version = db.relationship("OSVersion", backref="compute_instances", lazy=True)
