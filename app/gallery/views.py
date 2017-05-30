# -*- coding: utf-8 -*-
from flask import render_template, request
from . import gallery
from ..models import Picture
import json


@gallery.route('/api/gallery/more')
def api_gallery_more():
    count = request.args.get('count')
    pictures = Picture.query.filter(Picture.id > count).limit(5).all()
    sources_add = []
    for pic in pictures:
        sources_add.append('../static/image/gallery/'+pic.source)
    print sources_add
    return json.dumps(sources_add)


@gallery.route('/gallery')
def gallery():
    pictures = Picture.query.limit(25).all()
    sources = []
    for pic in pictures:
        sources.append('../static/image/gallery/'+pic.source)
    return render_template('gallery/gallery.html', sources=sources)
